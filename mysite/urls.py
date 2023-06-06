from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from shops.views import (
    shop_list, shop_detail, shop_create, shop_update, ShopQueryView, shop_get,
    shop_delete, admin_panel
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include([
        path('', shop_get, name='shop_get'),
        path('list/', login_required(shop_list), name='shop_list'),
        path('create/', login_required(shop_create), name='shop_create'),
        path('<int:shop_id>/', login_required(shop_detail), name='shop_detail'),
        path('<int:shop_id>/update/', login_required(shop_update), name='shop_update'),
        path('query/', login_required(ShopQueryView.as_view()), name='shop_query'),
        path('<int:shop_id>/delete/', login_required(shop_delete), name='shop_delete'),
        path('admin_panel/', login_required(admin_panel), name='admin_panel'),
    ])),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='base.html'), name='logout'),
    
    path('', shop_list, name='home'),
]
