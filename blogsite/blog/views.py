# blog/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Post

def frontpage(request):
    
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})
    


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect('post_detail', slug=post.slug)  # Corrected the redirect statement
    else:
        form = CommentForm()

    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})