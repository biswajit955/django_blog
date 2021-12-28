from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import decorator_from_middleware
from .middelware import UnderConstruction
from django.http import Http404


from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,

)


def base(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'blog/base.html', context)

# Create your views here.


def home(request):
    post_list = Post.objects.all()
    ip = request.session.get('ip', 0)
    print(ip)
    context = {
        'posts': post_list,
        'ip': ip
    }
    return render(request, 'blog/home.html', context)


@decorator_from_middleware(UnderConstruction)
def about(request):
    return render(request, 'blog/about.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 4
    paginate_orphans = 1
    ordering = ['-date_posted']

    def get_context_data(self, *args, **kwargs):
        try:
            context = super(PostListView, self).get_context_data(
                *args, **kwargs)
            context['ip'] = self.request.session.get('ip', 0)
            return context
        except Http404:
            # this is for , if any one got to more than available page than page go to first page
            self.kwargs['page'] = 1
            return super(PostListView, self).get_context_data(*args, **kwargs)


class PostDetailview(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, SuccessMessageMixin):
    model = Post
    template_name = 'blog/post_create.html'
    fields = ['title', 'content']

    # after post request url
    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("post-detail", kwargs={"pk": pk})

    def form_valid(self, form):
        form.instance.author == self.request.user
    # ------------------------------------
        print(form.instance.author)
        print(self.request.user)
    # ------------------------------------
        messages.info(self.request, f"Your post updated")
        return super().form_valid(form)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = '/'

    def form_valid(self):
        messages.error(self.request, f"Your post is deleted ")
        return HttpResponseRedirect(self.success_url)

    def test_func(self):
        Post = self.get_object()
        if self.request.user == Post.author:
            return True
        return False
