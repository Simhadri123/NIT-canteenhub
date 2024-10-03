from django.contrib import admin

# Register your models here.
from .models import *

# Get all model classes defined in models.py
model_classes = [cls for name, cls in globals().items() if isinstance(cls, type)]

# Register each model class with the admin site
for model_class in model_classes:
    admin.site.register(model_class)
