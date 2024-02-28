from django.shortcuts import render
from django.urls import reverse
from .models import Post
from django.db.models import Q

# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    # link = reverse('post_detail', args=[id])
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_search(request):

    content_q = request.GET.get('content_q')
    # title_q = request.GET.get('title_q')

    posts = Post.objects.all()

    if content_q:
        posts = posts.filter(Q(content__icontains = content_q) | Q(title__icontains = content_q)) 

    # if title_q:
    #     posts = posts.filter(title__icontains = title_q)

    return render(request, 'blog/post_search.html', {'posts': posts})