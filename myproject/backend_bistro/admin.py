from django.contrib import admin
from .models import MenuItems, Cuisine, Category

# Register your models here.

class MenuAdmin(admin.ModelAdmin):
    pass
admin.site.register(MenuItems, MenuAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)

class CuisineAdmin(admin.ModelAdmin):
    pass
admin.site.register(Cuisine, CuisineAdmin)