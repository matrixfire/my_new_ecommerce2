from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import BlogPost




def blog_list(request):
    blog_posts = BlogPost.objects.all()

    paginator = Paginator(blog_posts, 6)  # Show 10 blog posts per page

    page = request.GET.get('page')
    try:
        blog_posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page.
        blog_posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page.
        blog_posts = paginator.page(paginator.num_pages)

    return render(request, 'blogs/blog_list.html', {'posts': blog_posts})


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)
    return render(request, 'blogs/blog_detail.html', {'post': post})
