from django.contrib import admin
from .models import ToDoList, Item

# Registering models here
admin.site.register(ToDoList)
admin.site.register(Item)
