from django.contrib import admin
from gachon_flea.models import User, Product, Cart, ViewBuyList, ViewSellList, Comment, Review, BlackList, Category, Profile


# Register your models here.
@admin.register(Product)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'date',)
@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user', 'number',)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'product_id',)


@admin.register(ViewBuyList)
class ViewBuyList(admin.ModelAdmin):
    list_display = ('owner', 'product_id',)


@admin.register(ViewSellList)
class ViewSellList(admin.ModelAdmin):
    list_display = ('owner', 'product_id',)


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('owner', 'content',)


@admin.register(Review)
class Review(admin.ModelAdmin):
    list_display = ('owner', 'content',)


@admin.register(BlackList)
class BlackList(admin.ModelAdmin):
    list_display = ('user_id',)


