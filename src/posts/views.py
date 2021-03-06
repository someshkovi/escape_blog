from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Count, Q
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponseRedirect
from posts.forms import CommentForm, PostForm
from posts.models import Post, PostView
from accounts.models import Subscriber
from marketing.models import Signup


def contact(request):
    context = {}
    return render(request, 'blog/typewriter.html', context)

def get_author(user):
    qs = Subscriber.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query)
        ).distinct()
    context = {
        'queryset':queryset
    }
    return render(request, 'search_results.html', context)

def get_category_count():
    queryset = Post \
        .objects \
        .values('categories__title') \
        .annotate(Count('categories__title'))
    return queryset

def index(request):
    featured = Post.objects.filter(pub_date__lte=timezone.now()).filter(featured=True)
    latest = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[0:3]

    context = {
        'object_list':featured,
        'latest':latest
    }
    if request.method == "POST":
        email = request.POST['email']
        signup, created = Signup.objects.get_or_create(email=email)
        # new_signup.email = email
        # new_signup.save()
        if created:
            messages.success(request, f"{email} successfully subscribed")
        else:
            messages.warning(request, f"{email} already subscribed")
        return HttpResponseRedirect('/')

    return render(request, 'index.html', context)

def blog(request):
    category_count = get_category_count()
    most_recent = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
    post_list = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')
    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
        'most_recent' : most_recent,
        'category_count' : category_count,
    }
    return render(request, 'blog.html', context)

def post(request, id):
    category_count = get_category_count()
    most_recent = Post.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:3]
    post = get_object_or_404(Post, id=id)

    if request.user.is_authenticated:
        PostView.objects.get_or_create(user=request.user, post=post)

    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse('post-detail', kwargs={
                'id': post.id
            }))
    context = {
        'form': form,
        'post': post,
        'most_recent' : most_recent,
        'category_count' : category_count,
    }
    return render(request, 'post.html', context)

@login_required(login_url='account_login')
def post_create(request):
    title = 'Create'
    form = PostForm(request.POST or None, request.FILES or None)
    author = get_author(request.user)
    if author is None:
        Subscriber.objects.create(user=request.user)
        author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs = {
                'id': form.instance.id
            }))
    context = {
        'title':title,
        'form':form
    }
    return render(request, "post_create.html", context)

@login_required(login_url='account_login')
def post_update(request, id):
    title = 'Update'
    post = get_object_or_404(Post, id=id)
    form = PostForm(
        request.POST or None,
        request.FILES or None,
        instance=post)
    author = get_author(request.user)
    if request.method == "POST":
        if form.is_valid():
            form.instance.author = author
            form.save()
            return redirect(reverse('post-detail', kwargs = {
                'id': form.instance.id
            }))
    context = {
        'title':title,
        'form':form,
        'post':post
    }
    return render(request, "post_create.html", context)

@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect(reverse('post-list'))
    # post.delete()
    # return redirect(reverse('post-list'))

    context = {
        'post':post
    }

    return render(request, 'post_delete.html', context)
