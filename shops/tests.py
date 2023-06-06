from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Shop
from .forms import ShopForm
from django.views import View
from django.db.models import F, FloatField
from django.db.models.functions import Power, Sqrt

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required
def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})

@login_required
def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'shop_detail.html', {'shop': shop})

@login_required
def shop_get(request):
    return render(request, 'base.html')

@login_required
def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_list')
    else:
        form = ShopForm()
    return render(request, 'shop_create.html', {'form': form})

@login_required
def shop_update(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)

    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_detail', shop_id=shop_id)
    else:
        form = ShopForm(instance=shop)

    return render(request, 'shop_update.html', {'form': form, 'shop_id': shop_id})

@login_required
def shop_delete(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        shop.delete()
        return redirect('shop_list')
    return render(request, 'shop_confirm_delete.html', {'shop': shop})

class ShopQueryView(View):
    def get(self, request):
        return render(request, 'shop_query.html')
    
    def post(self, request):
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        distance = float(request.POST.get('distance'))

        shops = Shop.objects.annotate(
            lat_diff=Power(F('latitude') - latitude, 2),
            lon_diff=Power(F('longitude') - longitude, 2),
            distance=Sqrt(F('lat_diff') + F('lon_diff')),
        ).filter(distance__lte=distance)

        return render(request, 'shop_query_results.html', {'shops': shops})
