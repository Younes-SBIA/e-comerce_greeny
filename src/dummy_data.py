import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

import django
django.setup()


from faker import Faker
import random
from products.models import Product, Brand, Category

def seed_brand(n):
    fake = Faker()
    images = [
        '1.jpg',  '2.jpg',  '3.jpg',  '4.jpg',  '5.jpg',  '6.jpg',  '7.jpg',  '8.jpg'
    ]
    
    for _ in range(n):
        name = fake.name()
        image = f"brand/{images[random.randint(0, len(images)-1)]}"
        Brand.objects.create(name=name, image=image)
    print(f'Successfully Seeded {n} Brands')
    
    
def seed_category(n):
    fake = Faker()
    images = [
        '1.jpg',  '2.jpg',  '3.jpg',  '4.jpg',  '5.jpg',  '6.jpg',  '7.jpg',  '8.jpg' 
    ]
    for _ in range(n):
        name = fake.name()
        image = f"category/{images[random.randint(0, len(images)-1)]}"
        Category.objects.create(name=name, image=image)
        
    print(f'Successfully Seeded {n} Category')
    

def seed_product(n):
    fake = Faker()
    images = [
        '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg','6.jpg','7.jpg', '8.jpg', '9.jpg'
        ]
    flag_type = ['New', 'Feature', 'Sale']
    for _ in range(n):
        name = fake.name()
        sku = random.randint(0,10000)
        subtitle = fake.text(max_nb_chars=300)
        desc = fake.text(max_nb_chars=10000)
        flag = flag_type[random.randint(0,2)]
        price = round(random.uniform(20.99, 99.99),2)
        image = f"product/{images[random.randint(0, len(images)-1)]}"
        category = Category.objects.get(id =random.randint(3, 10))
        brand = Brand.objects.get(id = random.randint(3, 10))
        Product.objects.create(
            name=name, 
            sku=sku,
            subtitle=subtitle,
            desc=desc,flag=flag,
            price=price, 
            image=image, 
            category=category, 
            brand=brand,
            video_url="https://youtu.be/NEIP8bhkJVQ"
            )
    print(f'Successfully Seeded {n} Product')

seed_brand(50)
seed_category(50)
seed_product(100)

