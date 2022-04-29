from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Tweet
from .forms import TweetForm


class TweetListView(ListView):
    model = Tweet
    template_name = 'home.html'

class TweetCreateView(LoginRequiredMixin, CreateView):
    model = Tweet
    template_name = 'tweet_new.html'
    fields = ['body']

    def get_success_url(self):
        return reverse('tweets:home')

    def get_login_url(self):
        return reverse('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def index(request):
    tweets = Tweet.objects.order_by('-created_at')
    paginator = Paginator(tweets, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    form = TweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('tweets:index')
    else:
        form = TweetForm
        # return HttpResponseRedirect('/')

    try:
        paginated_queryset= paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
        'tweets' : tweets,
        'form' : form
    }
    return render(request, 'tweets/index.html', context)