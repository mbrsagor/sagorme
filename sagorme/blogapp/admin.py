from django.contrib import admin

from .models import *


# Register Post models
class Post_Admin(admin.ModelAdmin):

	list_display = ['title','category','author','posted_on','update']
	search_fields = ['title']

admin.site.register(Post, Post_Admin)



# Register Category models
class Category_admin(admin.ModelAdmin):

	list_display = ['name','created_at']

admin.site.register(Category, Category_admin)



# Register Author models
class Author_admin(admin.ModelAdmin):

	list_display = ['name','author_name','created_at']

admin.site.register(Author, Author_admin)



# Register Author models
class Widget_admin(admin.ModelAdmin):

	list_display = ['tagline']

admin.site.register(Widget, Widget_admin)



# Register Menus models
class Menu_admin(admin.ModelAdmin):

	list_display = ['name','menu_url','created_at']

admin.site.register(Menu, Menu_admin)




admin.site.register(Socail)