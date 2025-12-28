from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category
from django.db.models import Q

# Create your views here.
def posts_by_category(request, category_id):
    posts = Blog.objects.filter(category__id=category_id, status='Published')

    #Option 1: Using get_object_or_404
    category = get_object_or_404(Category, id=category_id)

    #Option 2: Using try-except 
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect("home")

    context = {
        'posts': posts,
        'category': category,
    }

    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog,
    }

    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }

    return render(request, 'search.html', context)