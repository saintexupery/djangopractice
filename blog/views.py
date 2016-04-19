from django.shortcuts import render
from .models import Post

def post_list(request):
    post_list = Post.objects.all()
    return render(request, 'blog/post_list.html',{
        'post_list' : post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post' : post,
    })