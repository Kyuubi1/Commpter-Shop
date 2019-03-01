
from django.contrib import admin
from .models import Account, Product, Category, Service, FixService, Cart
# Register your models here.

admin.site.site_header = "Meliodas"


class Admin(admin.ModelAdmin):
    list_display = ('username', 'email', 'sex', 'address', 'phone',  'is_active', 'is_staff', )


class ProductDT(admin.ModelAdmin):
    list_display = ('name', 'number', 'category', 'description', 'cost', 'image', )


admin.site.register(Account, Admin)
admin.site.register(Product, ProductDT)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(FixService)
admin.site.register(Cart)


