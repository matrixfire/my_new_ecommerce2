from django.shortcuts import render
from .models import News

def news(request):
    newss = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news.html', {'newss':newss})


def news_detail(request, news_id):
    news_content = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news_content': news_content})
