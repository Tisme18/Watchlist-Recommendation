#http://127.0.0.1:8000/admin
#un and pw: msys30 
from django.contrib import admin
from .models import Movie

admin.site.register(Movie)
