from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Author


def home(request):
    return render(request, 'home.html')

def posts(request):
    all_posts = Post.objects.all()

    return render(request, 'posts.html', {'posts': all_posts})

def post(request, post_id):
    post = Post.objects.get(id=post_id)

    return HttpResponse(f"<h1>{post.title}</1>")    