from contextlib import ContextDecorator
from AppWT.models import Posts
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model



# Vistas para el Blog

class PostList(ListView):
    model=Posts
    template_name= '03-blog.html'


class PostDetails(DetailView):
    model=Posts
    template_name= '03-1-readpost.html'

class CreatePost(CreateView):
    model=Posts
    success_url = reverse_lazy('blog')
    template_name = '03-2-createpost.html'
    fields = ['titulo', 'subtitulo', 'posteo', 'autor', 'image' ]

class ModifyPost(UpdateView):
    model=Posts
    template_name = '03-4-editpost.html'
    success_url = reverse_lazy('blog')
    fields = ['titulo', 'subtitulo', 'posteo']

class DeletePost(DeleteView):
    model=Posts
    template_name='03-3-deletepost.html'
    success_url = reverse_lazy('blog')






