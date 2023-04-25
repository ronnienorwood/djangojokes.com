from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from .models import Joke
from .forms import JokeForm


class JokeListView(ListView):
    model = Joke


class JokeDetailView(DetailView):
    model = Joke


class JokeCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke create successful.'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JokeUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = Joke
    form_class = JokeForm
    success_message = 'Joke update successful.'

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class JokeDeleteView(UserPassesTestMixin, DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')

    def delete(self, request, *args, **kwargs):
        result = super().delete(request, *args, **kwargs)
        return result

    def form_valid(self, form):
        messages.success(self.request, 'Joke delete successful.')
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user
