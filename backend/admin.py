from django.contrib import admin
from .models import TodoItem, Students

# Register your models here.

admin.site.register(TodoItem)
admin.site.register(Students)