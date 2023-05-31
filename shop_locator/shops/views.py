from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .forms import ShopForm
from django.views import View
from django.db.models import F, FloatField
from django.db.models.functions import Power, Sqrt

def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shop_list.html', {'shops': shops})

def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'shop_detail.html', {'shop': shop})
def shop_get(request):
    return render(request, 'base.html')
def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save()
            return redirect('shop_detail', shop_id=shop.pk)  # Redirect to shop detail page
    else:
        form = ShopForm()
    return render(request, 'shop_form.html', {'form': form})

def shop_update(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_list')
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_form.html', {'form': form})

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