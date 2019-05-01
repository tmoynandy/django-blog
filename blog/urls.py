from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"), ##will use the same PostCreateView template
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"), ##will use the same PostCreateView template
    path('about/', views.about, name="blog-about"),
]