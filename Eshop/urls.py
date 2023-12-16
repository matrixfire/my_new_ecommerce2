from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings


from django.contrib.sitemaps.views import sitemap

from store.sitemaps import StoreSitemap
from blogs.sitemaps import BlogSitemap
from news.sitemaps import NewsSitemap

sitemaps = {
    'blogs': BlogSitemap,
    'news': NewsSitemap,
    'store': StoreSitemap
}



urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # Customizing the admin URL
    path('my-admin-xuancai-led-version-1/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    path('blogs/' , include('blogs.urls')),
    path('news/' , include('news.urls')),
    path('' , include('store.urls')),

] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)