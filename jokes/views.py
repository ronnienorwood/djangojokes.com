from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Joke
from .forms import JokeForm


class JokeListView(ListView):
    model = Joke


class JokeDetailView(DetailView):
    model = Joke


class JokeCreateView(CreateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm


class JokeUpdateView(UpdateView):
    model = Joke
    # fields = ['question', 'answer']
    form_class = JokeForm


class JokeDeleteView(DeleteView):
    model = Joke
    success_url = reverse_lazy('jokes:list')
