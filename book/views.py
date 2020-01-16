from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class BookListView(ListView):
    model = Post
    template_name = 'home.html'

class BookDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

class BookCreateView(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['title', 'author', 'description',]

class BookUpdateView(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'description',]

class BookDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')