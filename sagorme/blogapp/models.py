from django.db import models
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from fontawesome.fields import IconField

# Create Category models class

class Category(models.Model):
	name = models.CharField(max_length = 30, unique=True, null=True, blank=True)
	created_at = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.name



# Create Category models class
class Author(models.Model):
	name = models.ForeignKey(User, on_delete= models.CASCADE)
	author_name = models.CharField(max_length = 30, unique=True, null=True, blank=True)
	author_bio = RichTextField()
	author_pic = models.ImageField(upload_to = 'user')
	created_at = models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.author_name




# Create Post models class
class Post(models.Model):
	title = models.CharField(max_length = 120, unique=True, null=True, blank=True)
	body = RichTextField()
	image = models.ImageField(upload_to = 'blog',blank = True, null = True)
	author = models.ForeignKey(Author, on_delete = models.CASCADE)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	posted_on = models.DateField(null = True, blank = True, auto_now = True, auto_now_add = False)
	update =  models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.title




# Create Widget Author profile class
class Widget(models.Model):
	tagline = models.CharField(max_length = 120)
	author_body = RichTextField()

	def __str__(self):
		return self.tagline




# Create Menus class
class Menu(models.Model):
	name = models.CharField(max_length = 35)
	menu_url = models.CharField(max_length = 120)
	created_at =  models.DateTimeField(auto_now = True, auto_now_add = False)

	def __str__(self):
		return self.name



# Create Social Media class
class Socail(models.Model):
	name = models.CharField(max_length = 20)
	solid_link = models.CharField(max_length = 120)
	icon = IconField()

	def __str__(self):
		return self.name