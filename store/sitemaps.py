from django.contrib.sitemaps import Sitemap
from .models import Category, Product

class YourModelSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated
