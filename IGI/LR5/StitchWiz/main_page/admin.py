from django.contrib import admin

from main_page.models import News, Question, Vacancy, Review, Coupon
# Register your models here.
admin.site.register(News)
admin.site.register(Question)
admin.site.register(Vacancy)
admin.site.register(Review)
admin.site.register(Coupon)
