from django.http import Http404, HttpRequest
from django.shortcuts import render

from .models import Post

# Create your views here.
def posts_list(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, "posts/post_list.html", {"posts": posts})

def author_posts_list(request: HttpRequest, author_id: int):
    posts = Post.objects.filter(author=author_id)
    return render(request, "posts/post_list.html", {"posts": posts})

def post_detail(request: HttpRequest, post_id: int):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404("Post not found")
    return render(request, "posts/post.html", {"post": post})






