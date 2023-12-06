from django.test import TestCase

# Create your tests here.


from pathlib import Path

# class YourModel(models.Model):
    # Assuming the HTML content is stored in a file named default_content.html
default_content_file = Path(__file__).resolve().parent / 'templates' / 'detail_page_base.html'

print(Path(__file__).resolve().parent)
# Read the content of the file
with open(default_content_file, 'r', encoding='utf-8') as file:
    default_content = file.read()

print(default_content)