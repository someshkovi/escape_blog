from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from tutorials.models import Tutorial, TutorialTopic
from tutorials.forms import TutorialTopicForm, TutorialForm
from typing import Dict, Any
# Create your views here.

class TutorialsListView(ListView):
    template_name = 'tutorials/tutorials-list.html'

    def get_queryset(self):
        self.tutorials = Tutorial.objects.all()
        return self.tutorials

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        return context


class TutorialsCreateview(LoginRequiredMixin, CreateView):
    model = Tutorial
    template_name = 'tutorials/tutorial_create_form.html'
    form_class = TutorialForm
    # fields = ['topic_title', 'topic_sub_title', 'content', 'slug', 'previous_topic', 'next_topic']

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super().form_valid(form)

class TutorialsTopicListView(ListView):

    template_name = 'tutorials/topic-list.html'

    def get_queryset(self):
        self.tutorial = get_object_or_404(Tutorial, slug=self.kwargs['slug'])
        return TutorialTopic.objects.filter(topic_title=self.tutorial)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['tutorial'] = self.tutorial
        return context

class TutorialsTopicCreateView(LoginRequiredMixin, CreateView):
    model = TutorialTopic
    template_name = 'tutorials/topic_update_form.html'
    form_class = TutorialTopicForm
    # fields = ['topic_title', 'topic_sub_title', 'content', 'slug', 'previous_topic', 'next_topic']

    def get_initial(self):
        topic_title = self.request.GET.get('slug')
        return {
            'topic_title':topic_title
        }

    def form_valid(self, form):
        # form.instance.created_by = self.request.user
        return super().form_valid(form)

class TutorialsTopicDetailView(DetailView):
    model = TutorialTopic
    template_name = 'tutorials/topic-detail.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        # context['tutorial'] = self.
        return context


class TutorialsTopicUpdateView(UpdateView):
    model = TutorialTopic
    fields = ['topic_title', 'topic_sub_title', 'content', 'slug', 'previous_topic', 'next_topic']
    template_name = 'tutorials/topic_update_form.html'