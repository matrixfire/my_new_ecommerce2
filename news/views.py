from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import time

def news(request):
    newss = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news2.html', {'newss':newss})


def news_detail(request, news_id):
    news_content = get_object_or_404(News, pk=news_id)
    return render(request, 'news/news_detail.html', {'news_content': news_content})




def load_more_news(request):
    page = int(request.GET.get('page', 1))
    items_per_page = 1  # Adjust this value based on your needs
    start = (page - 1) * items_per_page
    end = start + items_per_page

    newss = News.objects.all().order_by('-pub_date')[start:end]

    data = []
    for news in newss:
        data.append({
            'id': news.id,
            'headline': news.headline,
            'body': news.body,
            'pub_date': news.pub_date.strftime('%Y-%m-%d'),
            'image_url': news.image.url if news.image else '',
        })

    return JsonResponse({'data': data})
