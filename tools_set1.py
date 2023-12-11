from PIL import Image
import os
import re
import pyperclip





def get_image_size(image_path):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return width, height
    except Exception as e:
        print(f"Error: {e}")
        return None






def resize_images(source_folder, destination_folder, target_size=(300, 300), prefix='', suffix=''):
    """
    Resize all JPEG images from a source folder and save the resized images to a destination folder.

    Parameters:
    - source_folder: The path to the folder containing the original JPEG images.
    - destination_folder: The path to the folder where the resized images will be saved.
    - target_size: A tuple representing the target size of the resized images. Default is (300, 300).
    - prefix: Optional prefix to be added before the resized image name. Default is an empty string.
    - suffix: Optional suffix to be added after the resized image name. Default is an empty string.
    """
    # Ensure destination folder exists, create if not
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            # Build paths for source and destination images
            source_path = os.path.join(source_folder, filename)

            # Build the new filename with prefix and suffix
            base_name, extension = os.path.splitext(filename)
            new_filename = f"{prefix}{base_name}{suffix}{extension}"

            destination_path = os.path.join(destination_folder, new_filename)

            # Open the image
            with Image.open(source_path) as img:
                # Resize the image
                resized_img = img.resize(target_size)

                # Save the resized image to the destination folder
                resized_img.save(destination_path)
                print(f'{filename} saved.')

from PIL import Image
import os

def resize_and_rename_image(source_path, destination_folder, target_size=(300, 300), new_name='resized_image.png'):
    """
    Resize an image, rename it, and save it to a destination folder.

    Parameters:
    - source_path: The path to the original image.
    - destination_folder: The path to the folder where the resized and renamed image will be saved.
    - target_size: A tuple representing the target size of the resized image. Default is (300, 300).
    - new_name: The new name for the resized image. Default is 'resized_image'.
    """
    # Ensure destination folder exists, create if not
    os.makedirs(destination_folder, exist_ok=True)

    # Open the image
    with Image.open(source_path) as img:
        # Resize the image
        resized_img = img.resize(target_size)

        # Build the new filename
        base_name, extension = os.path.splitext(new_name)
        print('ext is: ', extension)
        new_filename = f"{base_name}{extension}"

        destination_path = os.path.join(destination_folder, new_filename)

        # Save the resized and renamed image to the destination folder
        print('Prepare to save.')
        resized_img.save(destination_path)
        print(f'File saved.')

# source_path =r'C:\Users\Administrator\Desktop\bill\my_new_ecommerce\store\static\assets\images\xuancai.png'
# w, h = get_image_size(source_path)
# print(w, h)
# desti_folder = r'C:\Users\Administrator\Desktop\bill\my_new_ecommerce\store\static\assets\images'
# resize_and_rename_image(source_path, desti_folder, target_size=(w//3, h//3) )

# get_image_size

# print(get_image_size(r'C:\Users\Administrator\Desktop\bill\my_new_ecommerce\store\static\assets\images\project-2.jpg'))

# source_folder = r'C:\Users\Administrator\Desktop\bill\test'
# des_folder = r'C:\Users\Administrator\Desktop\bill\test\a'
# sizes = []
# for filename in os.listdir(source_folder):
#     if filename.endswith(".jpg") and 'project' in filename:
#         # Build paths for source and destination images
#         source_path = os.path.join(source_folder, filename)

#         # Build the new filename with prefix and suffix
#         base_name, extension = os.path.splitext(filename)
#         # new_filename = f"{base_name}{suffix}{extension}"

#         # destination_path = os.path.join(destination_folder, new_filename)

#         # Open the image
#         # with Image.open(source_path) as img:
#         #     # Resize the image
#         #     resized_img = img.resize(target_size)

#         #     # Save the resized image to the destination folder
#         #     resized_img.save(destination_path)
#         #     print(f'{filename} saved.')
#         sizes.append(get_image_size(source_path))
#         # print(size)
# print(len(os.listdir(des_folder)), list(os.listdir(des_folder)))
# files = list(os.listdir(des_folder))
# counter = 1
# for filename, size in zip(files, sizes):
    
#     source_path = os.path.join(des_folder, filename)
#     destination_folder = des_folder
#     resize_and_rename_image(source_path, destination_folder, target_size=size, new_name=f'project-{counter}.jpg')
#     counter += 1














import re
def do_sub_based_on_reg(reg_obj, orginal_txt='', sub_txt=''):
    # namesRegex = re.compile(r'Agent \w+')
    # namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')
    # agentNamesRegex = re.compile(r'Agent (\w)\w*')
    # agentNamesRegex.sub(r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')
    import re, pyperclip
    if not orginal_txt:
        orginal_txt = pyperclip.paste()
    new_txt = reg_obj.sub(sub_txt, orginal_txt)
    print(new_txt)
    pyperclip.copy(new_txt)


# reg = re.compile(r'(href=)".*?"')
# reg = re.compile(r'(src=)".*?"')
# reg = re.compile(r'(srcset=)".*?"')
# do_sub_based_on_reg(reg, sub_txt=rf'\1""')


# .......................................................................................................................

print(3)

import os
import django

# Set the environment variable to the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Eshop.settings')
django.setup()

import csv
from store.models import Product, Category
from django.core.files import File
from urllib.request import urlopen
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
        # description=description,
        price=price,
        available=available,
    )
    if created:
        # product.price = 19.99
        product.description = description
        # ... other fields ...
        product.save()
    else:
        # Download and save the image from the URL
        img_temp = urlopen(image_url)
        product.image.save(os.path.basename(image_url), File(img_temp))
        print(f'Product created: {name}')

csv_path = 'products.csv'


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
                category_name= category_name, # 'Electronics',
                name= name, #　'Product Name',
                slug= slug, # 'product-name',
                image_url= image_url, # 'https://example.com/path/to/image.jpg',
                description= description, # 'Product description goes here.',
                price= price # 99.99,
            )



feed_data_from_csv(csv_path)


import re

def modify_html_tag(tag, html_code='', mode='w', text=''):
    # Create regex pattern for the specified HTML tag
    pattern = re.compile(rf"(<{tag}.*?>)(.*?)(<\/{tag}>)", re.DOTALL)
    if not html_code:
        html_code = pyperclip.paste()
    # Define substitution based on the mode parameter
    if mode == 'w':
        modified_html = pattern.sub(rf"\1{text}\3", html_code)
    elif mode == 'a':
        modified_html = pattern.sub(rf"\1\2{text}\3", html_code)
    elif mode == 'x':
        modified_html = pattern.sub(rf'\1<input type="text" value="\2">\3', html_code)
    else:
        raise ValueError("Invalid mode. Use 'w' or 'a'.")
    # Print the modified HTML code
    # print(modified_html)
    pyperclip.copy(modified_html)
    return modified_html


import re
import pyperclip
import uuid

def modify_html_tag(tag, html_code='', mode='w'):
    # List to keep track of input IDs
    input_ids = []

    # Create regex pattern for the specified HTML tag
    pattern = re.compile(rf"(<{tag}.*?>)(.*?)(<\/{tag}>)", re.DOTALL)

    if not html_code:
        html_code = pyperclip.paste()

    # Define substitution based on the mode parameter
    def replace_match(match):
        # Generate a unique identifier for the input tag
        unique_id = str(uuid.uuid4())

        # Keep track of the unique ID in the list
        input_ids.append(unique_id)

        # Use the original content of the tag as the default value for the input
        default_value = match.group(2)

        # Create the input tag with a unique id and default value
        input_tag = f'<input type="text" id="{unique_id}" name="{tag}_input" value="{default_value}">'

        return f"{match.group(1)}{input_tag}{match.group(3)}"

    # Use the sub method to perform the substitution
    modified_html = pattern.sub(replace_match, html_code)

    pyperclip.copy(modified_html)
    return modified_html, input_ids

# # Example usage:
# result = modify_html_tag('p', mode='w')
# modified_html, input_ids = result


# pyperclip.copy(modified_html)








def import_data_from_csv(csv_file_path):
    """
    Import data from a CSV file and save it to a Django model.

    Parameters:
    - csv_file_path: The path to the CSV file.

    Returns:
    - Number of records imported.
    """
    records_imported = 0

    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Customize the following lines based on your CSV structure and model fields
            name = row['name']
            description = row['description']
            price = float(row['price'])
            # Assuming you have a 'created_at' field in your model
            created_at = datetime.now()

            # Additional processing or data transformation if needed

            # Example: Creating a slug for the name
            slug = slugify(name)

            # Save the data to the model
            your_model_instance = YourModel(
                name=name,
                description=description,
                price=price,
                created_at=created_at,
                slug=slug,
            )
            your_model_instance.save()

            records_imported += 1

    return records_imported
