from django.contrib import admin
from .models import Director, Film, Country, Category
# Register your models here.

admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Film)
admin.site.register(Director)