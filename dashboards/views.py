from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from .forms import AddUserForm, EditUserForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }

    return render(request, 'dashboard/dashboard.html', context)

def categories(request):
    return render(request, 'dashboard/categories.html')

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm()
    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_category.html', context)

def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)

        if form.is_valid():
            form.save()
            return redirect('categories')
        else:
            print(form.errors)
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
        'category': category,
    }

    return render(request, 'dashboard/edit_category.html', context)

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('categories')

def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }

    return render(request, 'dashboard/posts.html', context)

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False) #temporarily save the form data
            post.author = request.user
            post.save()

            title = form.cleaned_data.get('title')
            post.slug = slugify(title) + '-' + str(post.id)
            post.save()
            return redirect('posts') 
        else:
            print(form.errors)
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_post.html', context)

def edit_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            post = form.save()
            title = form.cleaned_data.get('title')
            post.slug = slugify(title) + '-' + str(post.id)
            post.save() 
            return redirect('posts') 
        else:
            print(form.errors)
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'dashboard/edit_post.html', context)

def delete_post(request, post_id):
    post = get_object_or_404(Blog, id=post_id)
    post.delete()
    return redirect('posts')

def users(request):
    users = User.objects.all()
    context = {
        'users': users,
    }

    return render(request, 'dashboard/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    else:
        form = AddUserForm()

    context = {
        'form': form,
    }

    return render(request, 'dashboard/add_user.html', context)

def edit_user(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)
    else:
        form = EditUserForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('users')