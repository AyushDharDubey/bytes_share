from django.contrib import admin
from .models import File, Tag

admin.site.register([File, Tag])