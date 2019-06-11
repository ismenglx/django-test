from django.contrib import admin

# Register your models here.
from mongodbTest.models import Authors

admin.site.register(Authors)
