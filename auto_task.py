import os
import django
import csv, re
import requests


# Set the environment variable to the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eshop.settings')
django.setup()



from store.models import Product, Category
from django.core.files.base import ContentFile
from django.utils.text import slugify



def extract_urls(text):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(r'https?://[^\s,]+')

    # Use findall to extract all URLs from the text
    urls = re.findall(url_pattern, text)
    return urls


def create_product(category_name, name, slug, image_url, description, price, available=True):
    category, created = Category.objects.get_or_create(name=category_name, slug=slugify(category_name))
    product, created = Product.objects.update_or_create(
        category=category,
        name=name,
        slug=slug,
        price=price,
        available=available,
    )
    product.description = description

    # Download and save the image from the URL
    response = requests.get(image_url)
    if response.status_code == 200:
        img_temp = response.content
        product.image.save(os.path.basename(image_url), ContentFile(img_temp))
        print(f'Product {"created" if created else "updated"}: {name}')
    else:
        print(f'Error downloading image for product: {name}')


def feed_data_from_csv(csv_path):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            category_name = row['Categories']
            name = row['Name']
            slug = slugify(name)
            image_url = extract_urls(row['Images'])[0]
            description = row['Description']
            price = 0

            create_product(
                category_name=category_name,
                name=name,
                slug=slug,
                image_url=image_url,
                description=description,
                price=price
            )

csv_path = 'products_test.csv'
feed_data_from_csv(csv_path)
