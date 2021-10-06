from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    
)


# Create your views here.
def home(request):
    post_list = Post.objects.all()


    context = {
        'posts': post_list 
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class PostDetailview(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin , CreateView):
    model =  Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content' ]
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        #messages.success(request, f'Your account has been created, Now you able to login.')
        return super().form_valid(form )

    def my_fun(self, messages,request):
        messages = messages.success(request, f'Your account has been created, Now you able to login.')
        return super().my_fun( messages )



class PostUpdateView(LoginRequiredMixin , UpdateView):
    model =  Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content' ]
    # after post request url
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin , DeleteView):
    model =  Post
    template_name = 'blog/post_delete.html'
    success_url = '/'

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False