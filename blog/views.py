from django.shortcuts import render, get_object_or_404
##the get_object_404 is : either get me the data or send a 404
from django.http import HttpResponse
#importing Post model
from django.contrib.auth.models import User
from .models import Post
#list view
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
#so that unauthenticated users can't make posts
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


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
    #pagination
    paginate_by = 5
    ## to access by url : http://localhost:8000/?page=<page-number>

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

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    #to get the exact post that we need to update - to see if the user is updating the post
    def test_func(self):
        post = self.get_object()
        ##to check if current usr is author of the post
        if self.request.user == post.author :
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    #we have to add a success_url to finally delete andd redirect
    success_url = '/'
    # context_object_name = 'post'

    #to get the exact post that we need to update - to see if the user is updating the post
    def test_func(self):
        post = self.get_object()
        ##to check if current usr is author of the post
        if self.request.user == post.author :
            return True
        return False
        
class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html' #by default it looks for <app>/<model>_<view>.html
    context_object_name = 'posts'  # by default it is object

    #pagination
    paginate_by = 5
    ## to access by url : http://localhost:8000/?page=<page-number>

    def get_queryset(self):
        ##kwarg is query param of url
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
