from django.shortcuts import render
from .models import News
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import time

def news(request):
    newss = News.objects.all().order_by('-pub_date')
    return render(request, 'news/news2.html', {'newss':newss})


# def news_detail(request, news_id):
#     news_content = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/news_detail.html', {'news_content': news_content})



def news_detail(request, news_id, slug):
    # Assuming that your News model has a 'slug' field
    news_content = get_object_or_404(News, pk=news_id, slug=slug)
    
    # Customize the meta description and page title based on your needs
    meta_description = f"Custom meta description for {news_content.headline}"
    page_title = f"{news_content.headline} - Your News Page Title"
    
    return render(
        request,
        'news/news_detail.html',
        {
            'news_content': news_content,
            'meta_description': meta_description,
            'page_title': page_title,
        }
    )



def load_more_news(request):
    page = int(request.GET.get('page', 1))
    items_per_page = 3  # Adjust this value based on your needs
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
            'slug': news.slug,
        })

    return JsonResponse({'data': data})
