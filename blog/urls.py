from django.urls import path
from .views import (
    PostListView,
    PostDetailview,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    about,
    base,
    home,
    
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    #path('',home,name='home'),
    path('base/', base, name='base'),
    path('post/<int:pk>/', PostDetailview.as_view(), name='post-detail'),
    path('post/create', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', about, name='about'),
]