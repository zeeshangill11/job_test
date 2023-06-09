from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.shortcuts import render, redirect, reverse
from .models import Post
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect(reverse('posts:post_list'))

    return render(request, 'posts/delete_post.html', {'post': post})


@login_required(login_url='login')
def post_list(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'posts/post_list.html', {'posts': posts})


@login_required(login_url='login')
def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        user = request.user  # Get the currently logged-in user
        Post.objects.create(title=title, content=content, user=user)
        return redirect(reverse('posts:post_list'))
    return render(request, 'posts/add_post.html')
