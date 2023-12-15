from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import time

def news(request):
    newss = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'newss':newss})


def news_detail(request, news_id):
    news_content = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news_content': news_content})







# # Create your views here.
# def index(request):
#     return render(request, "posts/index.html")

def news_acquire(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0)
    end = int(request.GET.get("end") or (start + 9))

    # Generate list of posts
    data = []
    for i in range(start, end + 1):
        data.append(f"Post #{i}")

    # Artificially delay speed of response
    time.sleep(1)

    # Return list of posts
    return JsonResponse({
        "news": data
    })