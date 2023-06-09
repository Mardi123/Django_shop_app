from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from .models import Shop
from .forms import ShopForm
from django.views import View
from django.db.models import F, FloatField
from django.db.models.functions import Power, Sqrt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def admin_panel(request):
    return render(request, 'admin_panel.html')

@login_required
def shop_list(request):
    if request.user.is_superuser:
        # Admin user can view all shops
        shops = Shop.objects.all()
    else:
        shops = Shop.objects.filter(user=request.user)
    return render(request, 'shop_list.html', {'shops': shops})

@login_required
def shop_detail(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    return render(request, 'shop_detail.html', {'shop': shop})

def shop_get(request):
    return render(request, 'base.html')

@login_required
@csrf_protect
def shop_create(request):
    if request.method == 'POST':
        form = ShopForm(request.POST)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.user = request.user  # Set the user as the owner of the shop
            shop.save()
            return redirect('shop_list')  # Redirect to shop list page
    else:
        form = ShopForm()
    return render(request, 'shop_create.html', {'form': form})

@login_required
@user_passes_test(lambda u: u.is_superuser or u.shop_set.exists())
@csrf_protect
def shop_update(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if shop.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to update this shop.")
    if request.method == 'POST':
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()
            return redirect('shop_detail', shop_id=shop_id)
    else:
        form = ShopForm(instance=shop)
    return render(request, 'shop_update.html', {'form': form, 'shop_id': shop_id})


@login_required
@user_passes_test(lambda u: u.is_superuser or u.shop_set.exists())
@csrf_protect
def shop_delete(request, shop_id):
    shop = get_object_or_404(Shop, pk=shop_id)
    if shop.user != request.user and not request.user.is_superuser:
        return HttpResponseForbidden("You don't have permission to delete this shop.")
    if request.method == 'POST':
        shop.delete()
        return redirect('shop_list')
    return render(request, 'shop_confirm_delete.html', {'shop': shop})

@method_decorator(login_required, name='dispatch')
class ShopQueryView(View):
    @method_decorator(csrf_protect)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
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
