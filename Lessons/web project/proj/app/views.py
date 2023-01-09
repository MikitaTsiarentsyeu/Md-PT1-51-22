from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from .models import Post, Author
from .forms import AddPost, AddModelPost
import datetime
from django.contrib.auth.decorators import permission_required



def home(request):
    return render(request, 'home.html')

def posts(request):
    all_posts = Post.objects.all()
    viewed_posts = request.session.get("viewed_posts", {})
    return render(request, 'posts.html', {'posts': all_posts, "viewed_posts":viewed_posts, 'logo': "test"})

def post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        viewed_posts = request.session.get("viewed_posts", {})
        if post_id not in viewed_posts:
            viewed_posts[post.id] = 1
        else:
            viewed_posts[post.id] += 1
        request.session["viewed_posts"] = viewed_posts
        return render(request, 'post.html', {'post':post})
    except: 
        return HttpResponseNotFound()

@permission_required("app.add_post")
def add_post(request):
    
    if request.method == "POST":
        form = AddModelPost(request.POST, request.FILES)
        if form.is_valid():
            post_entry = Post()
            post_entry.title = form.cleaned_data['title']
            post_entry.subtitle = form.cleaned_data['subtitle']
            post_entry.content = form.cleaned_data['content']
            post_entry.post_type = form.cleaned_data['post_type']
            post_entry.image = form.cleaned_data['image']
            post_entry.isuued = datetime.datetime.now()
            post_entry.author = Author.objects.get(email=request.user.email)

            post_entry.save()

            return redirect('post', post_id=post_entry.id)
    else:
        form = AddModelPost()

    return render(request, 'add_post.html', {'form':form})