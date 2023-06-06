from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from shops.views import (
    shop_list, shop_detail, shop_create, shop_update, ShopQueryView, shop_get,
    shop_delete, admin_panel
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include([
        path('', shop_get, name='shop_get'),
        path('list/', shop_list, name='shop_list'),
        path('create/', shop_create, name='shop_create'),
        path('<int:shop_id>/', shop_detail, name='shop_detail'),
        path('<int:shop_id>/update/', shop_update, name='shop_update'),
        path('query/', ShopQueryView.as_view(), name='shop_query'),
        path('<int:shop_id>/delete/', shop_delete, name='shop_delete'),
        path('admin_panel/', admin_panel, name='admin_panel'),
    ])),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
    path('accounts/profile/', TemplateView.as_view(template_name='profile.html'), name='profile'),
    path('', shop_list, name='home'),
]
