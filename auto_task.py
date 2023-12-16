import os
import django
import csv, re
import requests
import pyperclip

# Set the environment variable to the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eshop.settings')
django.setup()



from store.models import Product, Category
from blogs.models import BlogPost
from news.models import News

from django.core.files.base import ContentFile
from django.utils.text import slugify



def extract_urls(text):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(r'https?://[^\s,]+')

    # Use findall to extract all URLs from the text
    urls = re.findall(url_pattern, text)
    return urls


def create_product(category_name, name, slug, image_url, description, price, available=True):
    category, _ = Category.objects.get_or_create(name=category_name, slug=slugify(category_name))
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




def create_blog(title, content, description_html='', image_url=''):
    # Check if the blog post already exists based on title
    blog, created = BlogPost.objects.update_or_create(
        title=title,
        defaults={
            'content': content,
            'description_html': description_html,
        }
    )

    # Download and save the image from the URL
    if not image_url:
        return
    response = requests.get(image_url)
    if response.status_code == 200:
        img_temp = response.content
        blog.image.save(os.path.basename(image_url), ContentFile(img_temp))
        print(f'Blog {"created" if created else "updated"}: {title}')
    else:
        print(f'Error downloading image for blog: {title}')



def create_news(headline, body, description_html='', image_url=''):
    # Check if the news post already exists based on headline
    news, created = News.objects.update_or_create(
        headline=headline,
        defaults={
            'body': body,
            'description_html': description_html,
        }
    )

    # Download and save the image from the URL
    if not image_url:
        return
    response = requests.get(image_url)
    if response.status_code == 200:
        img_temp = response.content
        news.image.save(os.path.basename(image_url), ContentFile(img_temp))
        print(f'News {"created" if created else "updated"}: {headline}')
    else:
        print(f'Error downloading image for news: {headline}')

def feed_product_data_from_csv(csv_path):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # for blow are customized!

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
            print(f'{name} Processed.')






def feed_blogs_data_from_csv(csv_path):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # for blow are customized!
            headline = row['Headline']
            body = row['Body']
            create_news(
                    headline=headline, 
                    body=body, 
                    description_html='', 
                    image_url=''
            )      
            print(f'{headline} Processed.')


def feed_news_data_from_csv(csv_path):
    with open(csv_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            # for blow are customized!
            title = row['Title']
            content = row['Content']
            description_html = row['Description_html']

            create_blog(
                    title=title, 
                    content=content, 
                    description_html='', 
                    image_url=''
            )
            print(f'{title} Processed.')




def create_csv_file(file_path, header_list, data_list=[], ):
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header to the CSV file
        csv_writer.writerow(header_list)

        # Write the data to the CSV file
        for row in data_list:
            csv_writer.writerow(row)

# header = [line.split('=')[0].strip().capitalize() for line in pyperclip.paste().strip().split('\n')]
# print(header)
# create_csv_file('news_test.csv', header)

'''
            title = row['Title']
            content = row['Content']
            image_url = extract_urls(row['Image'])[0]
            description_html = row['Description_html']

            create_blog(
                    title=title, 
                    content=content, 
                    description_html='', 
                    image_url=''
            )

            
            headline = row['Headline']
            body = row['Body']
            image_url = extract_urls(row['Image'])[0]
            description_html = row['Description_html']

            create_news(
                    headline=headline, 
                    body=body, 
                    description_html='', 
                    image_url=''
            )            


            

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


'''

# csv_path = 'products_test.csv'
# csv_path = 'blogs_test.csv'
csv_path = 'news_test.csv'
feed_data_from_csv(csv_path)