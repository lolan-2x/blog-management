from django.shortcuts import redirect, render,get_object_or_404
from .models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


def home(request):
    posts = Blog.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def edit_blog(request, blog_id):
    post = get_object_or_404(Blog, id=blog_id)

    if post.user != request.user:
        return redirect('view-all')  # ❌ block access

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.category = request.POST.get('category')
        post.excerpt = request.POST.get('excerpt')
        post.tags = request.POST.get('tags')

        if request.FILES.get('image'):
            post.image = request.FILES.get('image')

        post.save()
        return redirect('view-all')

    return render(request, 'edit-blog.html', {'post': post})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {
                'error': '❌ Username or password is incorrect'
            })

    return render(request, 'login.html')


@login_required
def delete_blog(request, id):
    post = get_object_or_404(Blog, id=id)

    if post.user != request.user:
        return redirect('view-all')  # ❌ block

    post.delete()
    return redirect('view-all')

def view_all(request):
    posts = Blog.objects.all().order_by('-created_at')
    return render(request, 'view-all.html', {'posts': posts})

@login_required
def add_blog(request):
    if request.method == 'POST':
        Blog.objects.create(
            user=request.user,   # 🔥 VERY IMPORTANT
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.user.username,
            category=request.POST.get('category'),
            excerpt=request.POST.get('excerpt'),
            tags=request.POST.get('tags'),
            image=request.FILES.get('image')
        )
        return redirect('view-all')

    return render(request, 'add-blog.html')

def blog_detail(request, id):
    post = get_object_or_404(Blog, id=id)
    return render(request, 'blog-detail.html', {'post': post})

