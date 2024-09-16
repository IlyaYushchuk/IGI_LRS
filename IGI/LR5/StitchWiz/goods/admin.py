from django.contrib import admin

from goods.models import Categories, Products, Order


admin.site.register(Order)



@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ('masters',)  # Удобный вид для связи "многие ко многим"
