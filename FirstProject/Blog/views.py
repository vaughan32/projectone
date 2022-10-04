from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from Blog.models import Blog
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class BlogListView(ListView):
    model = Blog
    template_name = 'Blog/home.html'
    context_object_name = 'blog_posts'
    ordering = ['-date_created']
    paginate_by = 3

class UseristView(ListView):
    model = Blog
    context_object_name = 'blog_posts'
    template_name = 'Blog/user_posts.html'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Blog.objects.filter(author = user).order_by('-date_created')






class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin,CreateView):
    model = Blog
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
  
class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Blog
    fields = ['title','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False


class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Blog

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.author:
            return True
        return False

    success_url = '/'

def about(request):
    return render(request,'Blog/about.html',{'DjangoTitle' : 'About'})

def contact(request):
    return render(request,'Blog/contact.html',{'DjangoTitle' : 'Contact'})