from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.hashers import check_password, make_password
from django.views import View

from .models import Product, Category, Carousel
from .middlewares.auth import auth_middleware
from django.http import HttpResponse
from django.urls import reverse

# rest of the code remains unchanged


def home_page(request):
    # return render(request, 'home.html')
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
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
                  'list.html', # or structure like this 'shop/product/list.html'
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'total_products': Product.objects.filter(available=True).count(),
                    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    meta_description = f"Elevate your spaces with our customizable COB and SMD LED solutions, with this {product.name}!"
    page_title = f"LED-{product.name}"
    return render(request,
                  'detail2.html',
                  {'product': product,
                   'meta_description': meta_description,
                   'page_title': page_title,
                   })


# views.py in one of your Django apps



class RobotsTxtView(View):
    def get(self, request, *args, **kwargs):
        # Assuming your robots.txt file is in the root directory of your Django project
        with open('robots.txt', 'r') as f:
            robots_txt_content = f.read()

        return HttpResponse(robots_txt_content, content_type='text/plain')






# class Cart(View):
#     def get(self, request):
#         ids = list(request.session.get('cart', {}).keys())
#         products = Product.get_products_by_id(ids)
#         print(products)
#         return render(request, 'cart.html', {'products': products})

# class CheckOut(View):
#     def post(self, request):
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         customer = request.session.get('customer')
#         cart = request.session.get('cart')
#         products = Product.get_products_by_id(list(cart.keys()))
#         print(address, phone, customer, cart, products)

#         for product in products:
#             print(cart.get(str(product.id)))
#             order = Order(
#                 customer=Customer(id=customer),
#                 product=product,
#                 price=product.price,
#                 address=address,
#                 phone=phone,
#                 quantity=cart.get(str(product.id))
#             )
#             order.save()
#         request.session['cart'] = {}
#         return redirect('cart')

# class ProductDetail(View):
#     def get(self, request, product_id):
#         product = Product.objects.get(pk=product_id)
#         return render(request, 'detail.html', {'product': product})

# class ProductFilter(View):
#     def post(self, request):
#         product = request.POST.get('product')
#         remove = request.POST.get('remove') # - or + for cart
#         cart = request.session.get('cart', {})
#         # cart = request.session.get('cart')
        
#         if cart:
#             quantity = cart.get(product)
#             if quantity:
#                 if remove:
#                     if quantity<=1:
#                         cart.pop(product)
#                     else:
#                         cart[product]  = quantity-1
#                 else:
#                     cart[product]  = quantity+1
#             else:
#                 cart[product] = 1
#         else:
#             cart = {}
#             cart[product] = 1

#         request.session['cart'] = cart
#         print('cart', request.session['cart'])
#         # return redirect(reverse('store:homepage'))
#         # print(redirect('store:homepage'), 'lalala')
#         return redirect('store:home')
#         # return HttpResponse("Hello, world!") # HttpResponse (A very simple response that includes a response code of 200 and a string of text that can be displayed in a web browser

#     def get(self, request):
#         return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
#         # return render(request, 'home.html')
#         # return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')


# def store(request):
#     cart = request.session.get('cart', {})
#     if not cart:
#         request.session['cart'] = {}

#     categories = Category.get_all_categories()
#     category_id = request.GET.get('category')
    
#     if category_id:
#         products = Product.get_all_products_by_category_id(category_id)
#     else:
#         products = Product.get_all_products()
#     data = {'products': products, 'categories': categories}
#     print('you are:', request.session.get('email'))
#     return render(request, 'store.html', data)



# class Login(View):
#     return_url = None

#     def get(self, request):
#         Login.return_url = request.GET.get('return_url')
#         return render(request, 'login.html')

#     def post(self, request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         customer = Customer.get_customer_by_email(email)
#         error_message = None

#         if customer and check_password(password, customer.password):
#             request.session['customer'] = customer.id
#             if Login.return_url:
#                 return HttpResponseRedirect(Login.return_url)
#             else:
#                 Login.return_url = None
#                 return redirect('homepage')
#         else:
#             error_message = 'Invalid credentials'

#         return render(request, 'login.html', {'error': error_message})

# def logout(request):
#     request.session.clear()
#     return redirect('login')

# class OrderView(View):
#     def get(self, request):
#         customer = request.session.get('customer')
#         orders = Order.get_orders_by_customer(customer)
#         print(orders)
#         return render(request, 'orders.html', {'orders': orders})

# class Signup(View):
#     def get(self, request):
#         return render(request, 'signup.html')

#     def post(self, request):
#         post_data = request.POST
#         first_name = post_data.get('firstname')
#         last_name = post_data.get('lastname')
#         phone = post_data.get('phone')
#         email = post_data.get('email')
#         password = post_data.get('password')

#         value = {'first_name': first_name, 'last_name': last_name, 'phone': phone, 'email': email}
#         error_message = self.validate_customer(Customer(first_name=first_name, last_name=last_name,
#                                                          phone=phone, email=email, password=password))

#         if not error_message:
#             customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
#             customer.password = make_password(customer.password)
#             customer.register()
#             return redirect('homepage')
#         else:
#             data = {'error': error_message, 'values': value}
#             return render(request, 'signup.html', data)

#     def validate_customer(self, customer):
#         error_message = None
#         if not customer.first_name:
#             error_message = 'Please enter your First Name'
#         elif len(customer.first_name) < 3:
#             error_message = 'First Name must be 3 characters or more'
#         elif not customer.last_name:
#             error_message = 'Please enter your Last Name'
#         elif len(customer.last_name) < 3:
#             error_message = 'Last Name must be 3 characters or more'
#         elif not customer.phone:
#             error_message = 'Enter your Phone Number'
#         elif len(customer.phone) < 10:
#             error_message = 'Phone Number must be 10 characters long'
#         elif len(customer.password) < 5:
#             error_message = 'Password must be 5 characters long'
#         elif len(customer.email) < 5:
#             error_message = 'Email must be 5 characters long'
#         elif customer.isExists():
#             error_message = 'Email Address Already Registered'

#         return error_message
