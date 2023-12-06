from django import template
from urllib.parse import quote

register = template.Library()

@register.simple_tag
def whatsapp_link(phone_number):
    # Format the phone number and create the WhatsApp link
    formatted_phone = quote(phone_number)
    return f'https://api.whatsapp.com/send?phone={formatted_phone}'
