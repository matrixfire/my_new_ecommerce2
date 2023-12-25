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
from pathlib import Path



def extract_urls(text):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(r'https?://[^\s,]+')
    # Use findall to extract all URLs from the text
    urls = re.findall(url_pattern, text)
    # I myself addding this not sure if it is necesaage 
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
# csv_path = 'news_test.csv'
# feed_data_from_csv(csv_path)


import os
import csv
from store.models import Product

def generate_csv(csv_file_path):
    products = Product.objects.all()

    # Get the field names dynamically from the Product model
    header = [field.name for field in Product._meta.get_fields()]

    # Get the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the directory if it doesn't exist
    relative_dir = 'auto_data'
    absolute_dir = os.path.join(script_dir, relative_dir)
    os.makedirs(absolute_dir, exist_ok=True)

    # Specify the relative path for the CSV file
    csv_file_path = os.path.join(absolute_dir, csv_file_path)

    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=header)
        writer.writeheader()  # Write the header
        print(header)
        for product in products:
            writer.writerow({field: getattr(product, field) for field in header})

    print(f'CSV file "{csv_file_path}" generated successfully.')







def update_from_csv2(csv_file_path):
    from store.models import Product, ProductImage, Category
    from django.utils.text import slugify


    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Update product data
        for row in reader:
            category_name = row['Categories']  # Assuming 'category' is the name of the category
            category_slug = slugify(category_name)
            print(f'{category_name}->{category_slug}')

            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

            product_name = row["Name"]
            product_slug = slugify(product_name)

            product = Product.objects.create(
                category = category,
                name = product_name,
                slug = product_slug,
            )
            print(f'{product_name} updated successfully.')




def update_from_csv(csv_file_path):
    from store.models import Product, ProductImage, Category
    from django.utils.text import slugify

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Update product data
        for row in reader:
            category_name = row['Categories']
            category_slug = slugify(category_name)

            # Get or create the category
            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

            product_name = row["Name"]
            product_slug = slugify(product_name)

            # Check if a product with the same name and category already exists
            existing_product = Product.objects.filter(name=product_name, category=category).first()

            if existing_product:
                # Product already exists, print a message
                print(f'{product_name} already exists.')
            else:
                # Create the product
                product = Product.objects.create(
                    category=category,
                    name=product_name,
                    slug=product_slug,
                )
                print(f'{product_name} created successfully.')


def update_from_csv3(csv_file_path):
    from store.models import Product, ProductImage, Category
    from django.utils.text import slugify

    # Mapping dictionary for CSV columns to model fields
    field_mapping = {
        # 'Categories': 'category',
        'Name': 'name',
        'Short description': 'short_description',
        'Description': 'description',

        # Add more mappings as needed
    }

    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Update product data
        for row in reader:
            # Extract CSV column names and map to model fields
            mapped_fields = {field_mapping[col]: value for col, value in row.items() if col in field_mapping}

            category_name = row['Categories']
            category_slug = slugify(category_name)

            # Get or create the category
            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

            # Check if a product with the same name and category already exists
            existing_product = Product.objects.filter(name=row['Name'], category=category).first()

            if existing_product:
                # Product already exists, check for changes
                changes = []
                for field, value in mapped_fields.items():
                    # Compare the value from the CSV with the existing product's value
                    if getattr(existing_product, field) != value:
                        # Update the field and log the change
                        setattr(existing_product, field, value)
                        changes.append(f'{field}: {getattr(existing_product, field)} -> {value}')

                if changes:
                    # Save the updated product and print the changes
                    existing_product.save()
                    print(f'{row["Name"]} updated successfully. Changes: {", ".join(changes)}')
                else:
                    # print(f'{row["Name"]} already exists and has no changes.')
                    pass
            else:
                # Create the product
                product = Product.objects.create(
                    category=category,
                    name=row['Name'],
                    slug=slugify(row['Name']),
                    **{k: v for k, v in mapped_fields.items() if k not in ('name', 'slug')}
                )
                print(f'{row["Name"]} created successfully.')



import csv, time, random
import requests
from django.core.files.base import ContentFile
from store.models import Product, ProductImage, Category
from django.utils.text import slugify
from PIL import Image


def download_image_from_url(url, filename):
    time.sleep(random.randint(1,5))
    response = requests.get(url)
    if response.status_code == 200:
        image_content = response.content

        # You may resize the image here if needed
        # image = Image.open(BytesIO(image_content))
        # resized_image = image.resize((desired_width, desired_height))
        # image_content = resized_image.tobytes()

        return ContentFile(image_content, name=filename)
    else:
        print(f'Failed to download image from {url}')
        return None



def update_from_csv4(csv_file_path, image_flag=False):

    
    # Mapping dictionary for CSV columns to model fields
    field_mapping = {
        # 'Categories': 'category',
        'Name': 'name',
        'Short description': 'short_description',
        'Description': 'description',

        # Add more mappings as needed
    }
    # extract_urls

    with open(csv_file_path, 'r', encoding='ISO-8859-1') as csvfile:
        reader = csv.DictReader(csvfile)

        # Update product data
        for row in reader:
            # Extract CSV column names and map to model fields
            mapped_fields = {field_mapping[col]: value for col, value in row.items() if col in field_mapping}

            category_name = row['Categories']
            category_slug = slugify(category_name)

            # Get or create the category
            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

            # Check if a product with the same name and category already exists
            existing_product = Product.objects.filter(name=row['Name'], category=category).first()


            if existing_product:
                # Product already exists, check for changes
                changes = []
                for field, value in mapped_fields.items():
                    # Compare the value from the CSV with the existing product's value
                    if getattr(existing_product, field) != value:
                        # Update the field and log the change
                        setattr(existing_product, field, value)
                        changes.append(f'{field}: {getattr(existing_product, field)} -> {value}')

                if changes:
                    # Save the updated product and print the changes
                    existing_product.save()
                    print(f'{row["Name"]} updated successfully. Changes: {", ".join(changes)}')
                else:
                    # print(f'{row["Name"]} already exists and has no changes.')
                    pass
            else:
                # Create the product
                product = Product.objects.create(
                    category=category,
                    name=row['Name'],
                    slug=slugify(row['Name']),
                    **{k: v for k, v in mapped_fields.items() if k not in ('name', 'slug')}
                )
                print(f'{row["Name"]} created successfully.')
                existing_product = product

            main_image_url = extract_urls(row['Images'])[0]
            other_image_urls = extract_urls(row['Images'])[1:]

            if image_flag:

                if main_image_url:
                    main_image_content = download_image_from_url(main_image_url, f'{row["Name"]}_main_image.jpg')
                    if main_image_content:
                        existing_product.main_image.save(f'{row["Name"]}_main_image.jpg', main_image_content)
                        print(f'Main image for {row["Name"]} updated successfully.')

                for i, image_url in enumerate(other_image_urls):
                    image_content = download_image_from_url(image_url, f'{row["Name"]}_image_{i}.jpg')
                    if image_content:
                        ProductImage.objects.create(product=existing_product, image=image_content)
                        print(f'Image {i + 1} for {row["Name"]} added successfully.')

# generate_csv('product_template.csv')

update_from_csv4(Path('auto_data') / 'product_test.csv', image_flag=True)