from django.shortcuts import render
from django.http import HttpResponse
#importing Post model
from .models import Post
#list view
from django.views.generic import ListView, DetailView, CreateView
#so that unauthenticated users can't make posts
from django.contrib.auth.mixins import LoginRequiredMixin


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
    template_name = 'blog/home.html' #by default it looks for <app>/<model>_<view>.html
    context_object_name = 'posts'  # by default it is object

    #newest post at top, oldest at bottom
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    # context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    # context_object_name = 'post'

    ##specify the fields of the form
    fields = ['title', 'content']

    ##overwrite form valid method to make django know the logged in user is the author
    def form_valid(self, form):
        form.instance.author = self.request.user
        #calling the parent class after overwrite
        return super().form_valid(form)
        ##needws to be redirected or error