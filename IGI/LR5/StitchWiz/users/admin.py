from django.contrib import admin

from users.models import User, Master


admin.site.register(User)
admin.site.register(Master)