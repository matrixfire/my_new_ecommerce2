from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import Product, Category, Carousel, HTML_DIY, ProductImage
from django.db import transaction

# rest of the code remains unchanged

class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        # Assuming your robots.txt file is in the root directory of your Django project
        with open('robots.txt', 'r') as f:
            robots_txt_content = f.read()

        return HttpResponse(robots_txt_content, content_type='text/plain')


def home_page(request):
    carousel = Carousel.objects.all()
    HTML_contents = HTML_DIY.objects.all()
    context = {
        'carousel': carousel,
        'home_page_diy': HTML_contents,
    }
    return render(request, 'home2.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'list.html',  # or structure like this 'shop/product/list.html'
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'total_products': Product.objects.filter(available=True).count(),
                   })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    
    # Retrieve all ProductImages, including the one just created
    product_images = product.images.all()

    meta_description = f"Elevate your spaces with our customizable COB and SMD LED solutions, with this {product.name}!"
    page_title = f"LED-{product.name}"

    return render(request, 'detail2.html', {
        'product': product,
        'product_images': product_images,
        'meta_description': meta_description,
        'page_title': page_title,
    })