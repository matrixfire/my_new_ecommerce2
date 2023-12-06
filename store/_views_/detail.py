from django.shortcuts import render , redirect , HttpResponseRedirect
from store.models.product import Products
from store.models.category import Category
from django.views import View



from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect




# Create your views here.
class ProductDetail(View):

    def get(self , request, product_id):
        # print()
        product = get_object_or_404(Products,pk=product_id)
        # reviews = Review.objects.filter(movie = movie)
        return render(request, 'detail.html', 
                    {'product':product, })

