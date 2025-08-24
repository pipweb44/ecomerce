from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # تسجيل الدخول والخروج
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # التسجيل
    path('register/', views.register_view, name='register'),
    
    # الملف الشخصي
    path('profile/', views.profile_view, name='profile'),
    
    # طلبات المستخدم
    path('my-orders/', views.my_orders_view, name='my_orders'),
    path('order/<uuid:order_id>/', views.order_detail_view, name='order_detail'),
]
