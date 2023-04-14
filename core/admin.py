from django.contrib import admin
from django.contrib.admin import StackedInline
from django.contrib.auth.models import Group

from core.models import Category, Product, ProductCategory, ProductsPhoto, Tags, ProductTags, Sales, SalesProducts


class ProductPhotosInline(StackedInline):
    model = ProductsPhoto
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # fields = ('name',)
    # exclude = ('name',)
    list_display = ['name', 'slug', 'id']
    list_display_links = ['name']
    search_fields = ['name', 'id']
    list_editable = ['slug']
    search_help_text = 'Поиск по названию и ID'
    readonly_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # fields = (('name', 'price'), 'slug')
    list_display = ['name', 'price', 'slug', 'id']
    list_display_links = ['name']
    search_fields = ['name', 'price']
    list_editable = ['slug']
    search_help_text = 'Поиск по названию и цене'
    inlines = [ProductPhotosInline]


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['product', 'category', 'id']
    search_fields = ['product', 'category', 'id']
    search_help_text = 'Поиск по продуктам, категориям и ID'


@admin.register(ProductsPhoto)
class ProductsPhotoAdmin(admin.ModelAdmin):
    list_display = ['product', 'photo', 'id']
    search_fields = ['product', 'id']
    search_help_text = 'Поиск по продуктам и ID'


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'id']
    list_display_links = ['name']
    search_fields = ['name', 'id']
    list_editable = ['slug']
    search_help_text = 'Поиск по названию и ID'


@admin.register(ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    list_display = ['product', 'tag', 'id']
    search_fields = ['product', 'tag', 'id']
    search_help_text = 'Поиск по продуктам, тэгам и ID'


@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    list_display = ['name', 'active', 'short_title', 'id']
    list_display_links = ['name']
    search_fields = ['name', 'id']
    list_editable = ['active', 'short_title']
    search_help_text = 'Поиск по названию и ID'


@admin.register(SalesProducts)
class SalesProductsAdmin(admin.ModelAdmin):
    list_display = ['product', 'sale', 'id']
    search_fields = ['product', 'sale', 'id']
    search_help_text = 'Поиск по продуктам, акциям и ID'


admin.site.unregister(Group)