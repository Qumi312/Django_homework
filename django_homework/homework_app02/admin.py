from django.contrib import admin
from .models import Client, Order, Product
# Register your models here.


@admin.register(Product)
class Product(admin.ModelAdmin):

    list_display = ["name", "description", "price", "quantity"]
    ordering = ["name"]
    list_per_page = 5
    search_fields = ["name"]

    fieldsets = [
        (
            "Наименование",
            {
                "classes": ["wide"],
                "fields": ["name"],
            },
        ),
        (
            "Подробности",
            {
                "description": "Описание товара",
                "fields": ["description"],
            },
        ),
        (
            "Цена",
            {
                'description': 'Цена товара',
                "fields": ["price"],
            },
        ),
        (
            "Количество",
            {
                "description": "Количество",
                'fields': ['quantity']
            },
        ),
    ]


@admin.register(Client)
class Client(admin.ModelAdmin):

    list_display = ["name", "email", "phone", "address"]
    ordering = ["name"]
    list_per_page = 5
    search_fields = ["name"]

    fieldsets = [
        (
            "Наименование",
            {
                "classes": ["wide"],
                "fields": ["name"],
            },
        ),
        (
            "Подробности",
            {
                "description": "Email пользователя",
                "fields": ["email"],
            },
        ),
        (
            "Цена",
            {
                'description': 'Телефон',
                "fields": ["phone"],
            },
        ),
        (
            "Количество",
            {
                "description": "Адрес",
                'fields': ['address']
            },
        ),
    ]


admin.site.register(Order)
