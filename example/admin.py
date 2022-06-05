from django.contrib import admin

# Register your models here.
from django_query.admin import QueryAdmin
from example.models import Book, Author, Country, Category, Shop


class BookAdmin(QueryAdmin):
    list_display = ("name", "author", "price", "published_date")
    list_filter = ("published_date",)
    search_fields = ("name", "author__name")


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "age")
    list_filter = ("country",)
    search_fields = ("name",)


admin.site.register(Author, AuthorAdmin)


class CountryAdmin(admin.ModelAdmin):
    list_display = ("name", "population")
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Country, CountryAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


class ShopAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_filter = ("name",)
    search_fields = ("name",)


admin.site.register(Shop, ShopAdmin)
