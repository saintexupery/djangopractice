from django.contrib import messages
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect, render, get_object_or_404
#from django.views.generic import CreateView
from .models import Post
from .forms import PostForm
from .forms import CommentForm2

def post_new(request):
    # http method
    # - GET : 빈 html form 을 보여준다.
    # - POST : 유저가 빈 html form 을 채워서 "입력완료" 버튼을 누르면, 서버로 POST 방식으로 전송이 됩니다.
    # HttpReuqest 를 통해 받을 수 있는 인자
    # - request.GET : QueryDict 이라는 dict 과 유사한 타입
    # - request.POST : QueryDict 이라는 dict 과 유사한 타입
    # - request.FILES : QueryDict 이라는 dict 과 유사한 타입
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            # 방법 1)
            # url = reverse('blog:post_detail', args=[post.pk])
            # return redirect(url)
            # 방법 2)
            # return redirect(post.get_absolute_url())
            # 방법 3)

            messages.success(request, '새로운 포스팅을 등록했습니다.')

            return redirect(post)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })

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