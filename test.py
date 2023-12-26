
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
            mapped_fields['description'] = 'test---' + mapped_fields['description']
            category_name = row['Categories']
            category_slug = slugify(category_name)

            # Get or create the category
            category, created = Category.objects.get_or_create(name=category_name, slug=category_slug)

            # Check if a product with the same name and category already exists
            existing_product = Product.objects.filter(name=row['Name'], category=category).first()


            if existing_product:
                # Update all fields (except 'name') of the existing product
                Product.objects.filter(id=existing_product.id).update(**{
                    field: value for field, value in mapped_fields.items() if field != 'name'
                })

                print(f'{row["Name"]} updated successfully.')
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

            # main_image_url = extract_urls(row['Images'])[0]
            # other_image_urls = extract_urls(row['Images'])[1:]

            # if image_flag:

            #     if main_image_url:
            #         main_image_content = download_image_from_url(main_image_url, f'{row["Name"]}_main_image.jpg')
            #         if main_image_content:
            #             existing_product.main_image.save(f'{row["Name"]}_main_image.jpg', main_image_content)
            #             print(f'Main image for {row["Name"]} updated successfully.')

            #     for i, image_url in enumerate(other_image_urls):
            #         image_content = download_image_from_url(image_url, f'{row["Name"]}_image_{i}.jpg')
            #         if image_content:
            #             ProductImage.objects.create(product=existing_product, image=image_content)
            #             print(f'Image {i + 1} for {row["Name"]} added successfully.')
                


t = """
<img class="alignnone size-full wp-image-3151" src="https://xcledchip.com/wp-content/uploads/2023/06/Product-Introduction.jpg" alt="" width="1140" height="48" />\n\n◆ Nominal CCT: 2,700K,3000K, 3500K,4000K,6500K\n\n◆ Minimum cut length: DC5V- every 12.5mm, DC12V- every 25mm, DC24V-every 50mm\n\n◆ Color Rendering Index: Ra＞90\n\n◆ Operation temperature: -10℃-+45℃\n\n◆ Storage temperature: -10℃-+60℃\n\n◆ Package method: 5meters/Reel, 480 LEDs/m\n\n◆ Beam angle: 160°\n\n4mm Width PCB Ultra Thin 5v/12v/24v 5w 480Led/m White Color IP20 Professional New technology, high density, dot-free COB Flexible Led Strip Light, 16.4ft/5metre reel linear led strip For Mirror, Stairway, Ceiling, Kitchen, Closet, Cabinets, Furniture, Cover, Display cases, Shelves, Car lighting, Exhibitions, Cove lighting applications and much more, Smart Cob Led Strip Factory &amp;Manufacturer.\n\n4mm Flexible Cob Led strip has 480 LEDs per metre behind a totally diffused COB style phosphor cover. Priced per meter, it can be cut and soldered to your exact specifications with its 12.5mm, 25mm or 50mm cut points, or it can be supplied on 5 metre reels. It has shorter cut points which improve flexibility at just 12.5mm, 25mm or 50mm, and a high CRI90 as standard. This is a technologically advanced LED tape for premium users who demand something more.\n\nThe self-adhesive Super Narrow 4mm width backed tape offers high color efficiency, uniform illumination, and a wide beam angle of 160 degrees. Priced per metre.\n\n<img class="alignnone size-full wp-image-3154" src="https://xcledchip.com/wp-content/uploads/2023/06/Scissor-Cutter-Line.jpg" alt="" width="1140" height="48" />\n<img class="size-full wp-image-2586 alignleft" src="https://xcledchip.com/wp-content/uploads/2023/05/4mm-cutter-line.jpg" alt="" width="1000" height="458" />\n\n<img class="size-full wp-image-2587 alignleft" src="https://xcledchip.com/wp-content/uploads/2023/05/4mm-24v.jpg" alt="" width="800" height="800" />\n<img class="alignnone size-full wp-image-3152" src="https://xcledchip.com/wp-content/uploads/2023/06/Product-Specification-Parameter.jpg" alt="" width="1140" height="48" />\n<table style="font-family: arial; border: 1px solid #333; border-collapse: ollapse; border-spacing: 0; padding: 0; margin: 0; text-align: center;" border="0" width="800" cellspacing="0" cellpadding="0">\n<tbody>\n<tr style="background: #dddddd; line-height: 20px; font-weight: bold; font-size: 14px; color: #0e0e0e;">\n<td width="199">Description (Width&amp;Length)</td>\n<td width="135">QTY Leds/Meter</td>\n<td width="117">Input Voltage(V)</td>\n<td width="127">Power(W)</td>\n<td width="119">Color Temperature(K)</td>\n<td style="border-right: none;" width="101">Waterproof</td>\n</tr>\n<tr>\n<td height="39">4mm*500</td>\n<td>480</td>\n<td>5v</td>\n<td>5w</td>\n<td>2700-6500k</td>\n<td style="border-right: none;">IP20</td>\n</tr>\n<tr>\n<td height="36">4mm*500</td>\n<td>480</td>\n<td>5v</td>\n<td>5w</td>\n<td>Red/Green/Blue/Yellow/Pink</td>\n<td style="border-right: none;">IP20</td>\n</tr>\n<tr>\n<td height="37">4mm*500</td>\n<td>480</td>\n<td>12v</td>\n<td>5w</td>\n<td>2700-6500k</td>\n<td style="border-right: none;">IP20</td>\n</tr>\n<tr>\n<td height="39">4mm*500</td>\n<td>480</td>\n<td>12v</td>\n<td>5w</td>\n<td>Red/Green/Blue/Yellow/Pink</td>\n<td style="border-right: none;">IP20</td>\n</tr>\n<tr>\n<td height="39">4mm*500</td>\n<td>480</td>\n<td>24v</td>\n<td>5w</td>\n<td>2700-6500k</td>\n<td style="border-right: none;">IP20</td>\n</tr>\n<tr>\n<td style="border-bottom: 0;" height="43">4mm*500</td>\n<td style="border-bottom: 0;">480</td>\n<td style="border-bottom: 0;">24v</td>\n<td style="border-bottom: 0;">5w</td>\n<td style="border-bottom: 0;">Red/Green/Blue/Yellow/Pink</td>\n<td style="border-bottom: 0; border-right: none;">IP20</td>\n</tr>\n</tbody>\n</table>\n&nbsp;
<img class="alignnone size-full wp-image-3151" src="https://xcledchip.com/wp-content/uploads/2023/06/Product-Introduction.jpg" alt="" width="1140" height="48" /><br><br>◆ Nominal CCT: 2,700K,3000K, 3500K,4000K,6500K<br><br>◆ Minimum cut length: DC5V- every 12.5mm, DC12V- every 25mm, DC24V-every 50mm<br><br>◆ Color Rendering Index: Ra＞90<br><br>◆ Operation temperature: -10℃-+45℃<br><br>◆ Storage temperature: -10℃-+60℃<br><br>◆ Package method: 5meters/Reel, 480 LEDs/m<br><br>◆ Beam angle: 160°<br><br>4mm Width PCB Ultra Thin 5v/12v/24v 5w 480Led/m White Color IP20 Professional New technology, high density, dot-free COB Flexible Led Strip Light, 16.4ft/5metre reel linear led strip For Mirror, Stairway, Ceiling, Kitchen, Closet, Cabinets, Furniture, Cover, Display cases, Shelves, Car lighting, Exhibitions, Cove lighting applications and much more, Smart Cob Led Strip Factory &amp;Manufacturer.<br><br>4mm Flexible Cob Led strip has 480 LEDs per metre behind a totally diffused COB style phosphor cover. Priced per meter, it can be cut and soldered to your exact specifications with its 12.5mm, 25mm or 50mm cut points, or it can be supplied on 5 metre reels. It has shorter cut points which improve flexibility at just 12.5mm, 25mm or 50mm, and a high CRI90 as standard. This is a technologically advanced LED tape for premium users who demand something more.<br><br>The self-adhesive Super Narrow 4mm width backed tape offers high color efficiency, uniform illumination, and a wide beam angle of 160 degrees. Priced per metre.<br><br><img class="alignnone size-full wp-image-3154" src="https://xcledchip.com/wp-content/uploads/2023/06/Scissor-Cutter-Line.jpg" alt="" width="1140" height="48" /><br><img class="size-full wp-image-2586 alignleft" src="https://xcledchip.com/wp-content/uploads/2023/05/4mm-cutter-line.jpg" alt="" width="1000" height="458" /><br><br><img class="size-full wp-image-2587 alignleft" src="https://xcledchip.com/wp-content/uploads/2023/05/4mm-24v.jpg" alt="" width="800" height="800" /><br><img class="alignnone size-full wp-image-3152" src="https://xcledchip.com/wp-content/uploads/2023/06/Product-Specification-Parameter.jpg" alt="" width="1140" height="48" /><br><table style="font-family: arial; border: 1px solid #333; border-collapse: ollapse; border-spacing: 0; padding: 0; margin: 0; text-align: center;" border="0" width="800" cellspacing="0" cellpadding="0"><br><tbody><br><tr style="background: #dddddd; line-height: 20px; font-weight: bold; font-size: 14px; color: #0e0e0e;"><br><td width="199">Description (Width&amp;Length)</td><br><td width="135">QTY Leds/Meter</td><br><td width="117">Input Voltage(V)</td><br><td width="127">Power(W)</td><br><td width="119">Color Temperature(K)</td><br><td style="border-right: none;" width="101">Waterproof</td><br></tr><br><tr><br><td height="39">4mm*500</td><br><td>480</td><br><td>5v</td><br><td>5w</td><br><td>2700-6500k</td><br><td style="border-right: none;">IP20</td><br></tr><br><tr><br><td height="36">4mm*500</td><br><td>480</td><br><td>5v</td><br><td>5w</td><br><td>Red/Green/Blue/Yellow/Pink</td><br><td style="border-right: none;">IP20</td><br></tr><br><tr><br><td height="37">4mm*500</td><br><td>480</td><br><td>12v</td><br><td>5w</td><br><td>2700-6500k</td><br><td style="border-right: none;">IP20</td><br></tr><br><tr><br><td height="39">4mm*500</td><br><td>480</td><br><td>12v</td><br><td>5w</td><br><td>Red/Green/Blue/Yellow/Pink</td><br><td style="border-right: none;">IP20</td><br></tr><br><tr><br><td height="39">4mm*500</td><br><td>480</td><br><td>24v</td><br><td>5w</td><br><td>2700-6500k</td><br><td style="border-right: none;">IP20</td><br></tr><br><tr><br><td style="border-bottom: 0;" height="43">4mm*500</td><br><td style="border-bottom: 0;">480</td><br><td style="border-bottom: 0;">24v</td><br><td style="border-bottom: 0;">5w</td><br><td style="border-bottom: 0;">Red/Green/Blue/Yellow/Pink</td><br><td style="border-bottom: 0; border-right: none;">IP20</td><br></tr><br></tbody><br></table><br>&nbsp;

"""
import pyperclip as p
import re
from bs4 import BeautifulSoup



html_code = re.sub(r'\n', '<br>', t.strip())
print(html_code)
soup = BeautifulSoup(html_code, 'html.parser')
last_table = soup.find_all('table')[-1]

# Create a new h2 tag
for _ in range(1):
    new_h2_tag = soup.new_tag('h2')
    new_h2_tag.string = 'hello'

    # Insert the new h2 tag before the last table element
    last_table.insert_before(new_h2_tag)

tables = soup.find_all('table')

# Remove <br> tags within each table
for table in tables:
    for br_tag in table.find_all('br'):
        br_tag.extract()

# Get the modified HTML content
modified_html = str(soup)


# Prettify the modified HTML
prettified_html = soup.prettify()

print(prettified_html)
# print(prettified_html)
p.copy(modified_html)