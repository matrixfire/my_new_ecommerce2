class Language:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def message(self):
        print("My name is " + self.name)

languages = [Language("Python"), Language("JavaScript")]

for language in languages:
    language.message()




import csv
import requests
from django.core.files.base import ContentFile
from store.models import Product, ProductImage, Category
from django.utils.text import slugify
from PIL import Image


def download_image_from_url(url, filename):
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



def update_from_csv_with_images(csv_file_path):
    # Existing code ...

    for row in reader:
        # Existing code ...

        # Check if a product with the same name and category already exists
        existing_product = Product.objects.filter(name=row['Name'], category=category).first()

        if existing_product:
            # Existing code ...

            # Download image from URL and update main_image
            main_image_url = row.get('Main Image URL')
            if main_image_url:
                response = requests.get(main_image_url)
                if response.status_code == 200:
                    # Open the image using PIL to resize if needed
                    image = Image.open(BytesIO(response.content))

                    # You may resize the image here if needed
                    # resized_image = image.resize((desired_width, desired_height))
                    # image = resized_image

                    # Save the image to the main_image field using ContentFile
                    existing_product.main_image.save(f'{row["Name"]}_main_image.jpg', ContentFile(response.content))

                    print(f'Main image for {row["Name"]} updated successfully.')
                else:
                    print(f'Failed to download main image for {row["Name"]}')

            # Create ProductImage instances from image URLs
            image_urls = row.get('Image URLs', '').split(';')
            for image_url in image_urls:
                response = requests.get(image_url)
                if response.status_code == 200:
                    # Open the image using PIL
                    image = Image.open(BytesIO(response.content))

                    # Save the image to ProductImage field using ContentFile
                    ProductImage.objects.create(product=existing_product, image=ContentFile(response.content))

                    print(f'Image for {row["Name"]} added successfully.')
                else:
                    print(f'Failed to download image for {row["Name"]}')
                    
        else:
            # Existing code ...

