from django.contrib import admin
from django.urls import path  , include
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    
    # Customizing the admin URL
    path('my-admin-xuancai-led-version-1/', admin.site.urls),
    path('blogs/' , include('blogs.urls')),
    path('news/' , include('news.urls')),
    path('' , include('store.urls')),

] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)