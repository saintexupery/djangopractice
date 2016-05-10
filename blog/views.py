from django.shortcuts import render, redirect
from .models import Post
from .forms import CommentForm2

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

def comment_new(request, post_pk):
#    form = CommentForm()
    try:
        post = Post.objects.get(pk=post_pk)
    except Post.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = CommentForm2(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save
            return redirect(post)
    else:
        form = CommentForm2()
    return render(request, 'blog/comment_form.html', {
        'form': form
    })
# 위와 같은 코드는
# post -new = CreatView.as_view(model=Post, form_class=PostForm)