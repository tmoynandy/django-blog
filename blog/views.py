from django.shortcuts import render
from django.http import HttpResponse
#importing Post model
from .models import Post
#list view
from django.views.generic import ListView

# #dummy data
# posts = [
#     {
#         'author' : 'TanuN',
#         'title' : 'blog1',
#         'content' : 'aaaaa',
#         'date_posted' : '9/11/1996'
#     },
#     {
#         'author' : 'Tanumoy',
#         'title' : 'blog2',
#         'content' : 'aaaaabbbb',
#         'date_posted' : '9/11/1997'
#     },
#     {
#         'author' : 'TanuNandy',
#         'title' : 'blog3',
#         'content' : 'aaaaaccccc',
#         'date_posted' : '9/11/1998'
#     },
# ]
# Create your views here.

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})

# def home(request):
#     context = {
#         'posts' : Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context, {'title' : 'Home'})

##class based view of home instead of method based
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'