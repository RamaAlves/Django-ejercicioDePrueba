from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    fields = ('title',)

admin.site.register(Category, CategoryAdmin)

#decorador
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category')
    #fields = ('title', 'description', 'price', 'category')

#el decorador reemplaza la siguiente funcion
#admin.site.register(Product, ProductAdmin)