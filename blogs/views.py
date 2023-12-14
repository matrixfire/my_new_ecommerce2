from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost




def blog_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blogs/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blogs/blog_detail.html', {'post': post})
