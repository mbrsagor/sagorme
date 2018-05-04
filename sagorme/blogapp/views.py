from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *



# Create Home page views
def home(request):

	blog_obj = Post.objects.all().order_by('-id')
	widget_obj = Widget.objects.all()
	menu_obj = Menu.objects.all()
	social_obj = Socail.objects.all()

	# search query
	query = request.GET.get('q')
	if query:
		blog_obj = blog_obj.filter(title__icontains = query)
	
	# Pagination
	paginator = Paginator(blog_obj, 4)
	page = request.GET.get('page')
	total_aricel = paginator.get_page(page)
	
	context = {
		'posts' : total_aricel,
		'widget' : widget_obj,
		'menus' : menu_obj,
		'fnt' : social_obj,
	}
	return render(request, 'blogapp/index.html', context)



# Create Single page views
def single_page(request, id):

	single_obj = get_object_or_404(Post, id = id)
	widget_obj = Widget.objects.all()
	menu_obj = Menu.objects.all()
	social_obj = Socail.objects.all()
	related_post = Post.objects.filter(category = single_obj.category).exclude(id = id)[:3]

	context = {
		'single_obj' : single_obj,
		'widget' : widget_obj,
		'menus' : menu_obj,
		'fnt' : social_obj,
		'related_post' : related_post
	}
	return render(request, 'blogapp/single.html',context)



# Create Widget views
# def widget(request):

# 	widget_obj = Widget.objects.all()
# 	context = {
# 		'widget' : widget_obj
# 	}
# 	print("hello sagor")
# 	return render(request, 'app/base.html',context)



# Create category views
def category(request, name):

	post_list = Post.objects.filter(category__name = name).order_by('-id')
	widget_obj = Widget.objects.all()
	menu_obj = Menu.objects.all()
	social_obj = Socail.objects.all()

	context = {
		'post_list' : post_list,
		'widget' : widget_obj,
		'menus' : menu_obj,
		'fnt' : social_obj,
	}
	return render(request, 'blogapp/category.html',context)




# Create author views
def author(request, id):

	author_list = Post.objects.filter(author__id = id)
	widget_obj = Widget.objects.all()
	menu_obj = Menu.objects.all()
	social_obj = Socail.objects.all()

	context = {
		'author_list' : author_list,
		'widget' : widget_obj,
		'menus' : menu_obj,
		'fnt' : social_obj,
	}
	return render(request, 'blogapp/authors.html', context)