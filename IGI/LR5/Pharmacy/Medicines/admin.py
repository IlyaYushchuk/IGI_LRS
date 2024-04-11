from django.contrib import admin
from .models import Departments, Categories, Medicines

admin.site.register(Departments)
admin.site.register(Categories)
admin.site.register(Medicines)