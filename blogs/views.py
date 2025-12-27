from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category

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