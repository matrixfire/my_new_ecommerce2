
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