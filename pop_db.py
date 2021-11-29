import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'filmproject.settings')
django.setup()

from films.models import Country, Director, Category

from faker import Faker

f = Faker()

for cat_name in ['Comedy', 'Drama', 'War', 'Action', 'Superhero', 'Animated']:
    Category.objects.get_or_create(name=cat_name)

if Country.objects.count() < 10:
    country_set = set()
    while len(country_set) < 10:
        country_set.add(f.country())

    for name in country_set:
        Country.objects.get_or_create(name=name)


