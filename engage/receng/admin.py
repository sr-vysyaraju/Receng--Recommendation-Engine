from django.contrib import admin
from .models import Movie, Profile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

#registering movie model
admin.site.register(Movie)
#registering profile model
admin.site.register(Profile)