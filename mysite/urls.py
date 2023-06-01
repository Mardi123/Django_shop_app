from django.contrib import admin
from django.urls import path, include
from shops.views import shop_list, shop_detail, shop_create, shop_update, ShopQueryView, shop_get, shop_delete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops/', include([
        path('', shop_get, name = 'shop_get'),
        path('list/', shop_list, name='shop_list'),
        path('create/', shop_create, name='shop_create'),
        path('<int:shop_id>/', shop_detail, name='shop_detail'),
        path('<int:shop_id>/update/', shop_update, name='shop_update'),
        path('query/', ShopQueryView.as_view(), name='shop_query'),
        path('<int:shop_id>/delete/',  shop_delete, name= 'shop_delete')
    ])),
    # Add a default URL pattern to handle the root URL
    path('', shop_list, name='home'),
]
