from django.db import models
import datetime
from ckeditor.fields import RichTextField
from pathlib import Path

from django.urls import reverse

from django.utils import timezone  # Import timezone module


current_directory = Path.cwd()
relative_path = "templates/detail_page_base.html"
detail_page_file_path = current_directory / relative_path





class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        try:
            return reverse('store:product_list_by_category',
                       args=[self.slug])
        except:
            return 'some_url'

class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to= 'uploads/products/', # or like s'products/%Y/%m/%d'
                              blank=True)
    description = RichTextField() #  models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2, blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Add the last_modified_field
    # last_modified = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('store:product_detail',
                       args=[self.id, self.slug])

    # not sure if this coold with last_modified is necessary but just do it to test
    def save(self, *args, **kwargs):
        # Update last_modified_field whenever the model is saved
        # self.last_modified = timezone.now()
        self.updated = timezone.now()
        super().save(*args, **kwargs)



class Carousel(models.Model):
    # image       = models.ImageField(upload_to="pics/%y/%m/%d/")
    image       = models.ImageField(upload_to="pics/")
    title       = models.CharField(max_length=150)
    action_name = models.CharField(max_length=50)
    link        = models.TextField(null=True, blank=True)
    sub_title   = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title



class HTML_DIY(models.Model):
    name = models.CharField(max_length=150)
    html_content = RichTextField(blank=True)

    def __str__(self):
        return self.name



# class Category(models.Model):
#     name = models.CharField(max_length=50)

#     @staticmethod
#     def get_all_categories():
#         return Category.objects.all()

#     def __str__(self):
#         return self.name

# class Customer(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     phone = models.CharField(max_length=10)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)

#     def register(self):
#         self.save()

#     @staticmethod
#     def get_customer_by_email(email):
#         try:
#             return Customer.objects.get(email=email)
#         except Customer.DoesNotExist:
#             return None

#     def isExists(self):
#         return Customer.objects.filter(email=self.email).exists()

# class Order(models.Model):
#     product = models.ForeignKey('Products', on_delete=models.CASCADE)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)
#     price = models.IntegerField()
#     address = models.CharField(max_length=50, default='', blank=True)
#     phone = models.CharField(max_length=50, default='', blank=True)
#     date = models.DateField(default=datetime.datetime.today)
#     status = models.BooleanField(default=False)

#     def place_order(self):
#         self.save()

#     @staticmethod
#     def get_orders_by_customer(customer_id):
#         return Order.objects.filter(customer=customer_id).order_by('-date')


def read_html_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return ''
    except Exception as e:
        print(f"Error reading file: {e}")
        return ''
# default_description_html = read_html_from_file(file_path)
# print(default_description_html)


# class Products(models.Model):

#     # Read the content of the file


#     name = models.CharField(max_length=60)
#     price = models.IntegerField(default=0)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
#     # description = models.CharField(max_length=250, default='', blank=True, null=True)
#     # default_description_html = 
#     description = RichTextField(    )
#     '''<p>This is a random discription for description that uses words and imgs from other sites.<img alt="test_pet" src="https://images.pexels.com/photos/62289/yemen-chameleon-chamaeleo-calyptratus-chameleon-reptile-62289.jpeg?auto=compress&amp;cs=tinysrgb&amp;w=1260&amp;h=750&amp;dpr=1" style="height:750px; width:498px" /></p>'''
#     image = models.ImageField(upload_to='uploads/products/')

#     # @staticmethod
#     def change_product_detail_info(self):
#         default_content_file = Path(__file__).resolve().parent / 'templates' / 'detail_page_base.html'

#         # Read the content of the file
#         with open(default_content_file, 'r', encoding='utf-8') as file:
#             default_content = file.read()
#         self.description = default_content
#         self.save()
#         print('did!')


#     @staticmethod
#     def change_products_detail_info(changed_text=''):
#         for product in Products.objects.all():
#             product.description = changed_text
#             product.save()
#             print('Changed made!')


#     @staticmethod
#     def get_products_by_id(ids):
#         return Products.objects.filter(id__in=ids)

#     @staticmethod
#     def get_all_products():
#         return Products.objects.all()

#     @staticmethod
#     def get_all_products_by_category_id(category_id):
#         if category_id:
#             return Products.objects.filter(category=category_id)
#         else:
#             return Products.get_all_products()



