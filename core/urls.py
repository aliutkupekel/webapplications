from django.contrib.auth import views as auth_views
from django.urls import path, include #also we added include and we need also path here 
from . import views
from django.conf import settings
from django.conf.urls.static import static
#to register router in urls.py
from rest_framework.routers import DefaultRouter
from core.views import PostViewSet
from rest_framework.authtoken.views import obtain_auth_token # we added this as import for auth_token


# DRF router registeration
router = DefaultRouter()
router.register(r'api/posts', PostViewSet, basename='post')

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_post, name='create_post'),
    path('posts/', views.post_list, name='post_list'),
    path('success/', views.post_success, name='post_success'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='core/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='core/password_change_done.html'), name='password_change_done'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('posts/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('posts/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('api/token/', obtain_auth_token, name='api_token_auth'), # auth_token

    # we adding here DRF endpoints
    path('', include(router.urls)),

    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
