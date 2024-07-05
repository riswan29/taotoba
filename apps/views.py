from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
# Create your views here.

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'admin':
                    return redirect('admin:index')
                else:
                    return redirect('user_dash')
            else:
                return HttpResponse("Invalid credentials")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_dashboard(request):
    return render(request, 'user/index.html')

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_post')
    else:
        form = BlogPostForm()
    return render(request, 'fitur/create_blog.html', {'form': form})

@login_required
def blog_post(request):
    posts = BlogPost.objects.all()
    return render(request, 'fitur/blog_post.html', {'posts': posts})