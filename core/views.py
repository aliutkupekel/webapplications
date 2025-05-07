from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import login  # Eksikse ekle
from .forms import PostForm, UserUpdateForm, ProfileForm, RegisterForm  # RegisterForm varsa
from .models import Post, Profile
from django.contrib.auth.models import Group

def is_admin(user):
    return user.groups.filter(name='admins').exists()

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

def post_list(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {'posts': posts})

def profile(request):
    return render(request, 'core/profile.html')

def home(request):
    return render(request, 'core/home.html', {'message': 'Welcome to the Bloglife'})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def post_success(request):
    return render(request, 'success.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # veya kendi RegisterForm'unuz varsa onu kullanın
        if form.is_valid():
            user = form.save()
            # Profile zaten post_save ile oluşturulmalı
            try:
                group = Group.objects.get(name='Students of Mans')
                group.user_set.add(user)
            except Group.DoesNotExist:
                print("Hata: 'Students of Mans' grubu bulunamadı.")
            login(request, user)  # Kullanıcıyı otomatik oturum aç
            return redirect('home')  # Doğrudan anasayfaya yönlendir
    else:
        form = UserCreationForm()
    return render(request, 'core/register.html', {'form': form})

@login_required
def edit_profile(request):
    profile = request.user.profile  # Zaten sinyalde oluşturulduğu varsayılır

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    return render(request, 'core/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def profile_view(request):
    return render(request, 'core/profile.html', {
        'user': request.user,
        'profile': request.user.profile,
    })
