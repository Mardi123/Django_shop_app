from django.test import TestCase
from django.urls import reverse
from .models import Shop

class ShopTestCase(TestCase):
    def setUp(self):
        self.shop = Shop.objects.create(name='Shop 1', address='Address 1', contact='Contact 1', description='Description 1')

    def test_shop_list_view(self):
        response = self.client.get(reverse('shop_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.shop.name)

    def test_shop_detail_view(self):
        response = self.client.get(reverse('shop_detail', args=[self.shop.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.shop.name)
        self.assertContains(response, self.shop.address)
        self.assertContains(response, self.shop.contact)
        self.assertContains(response, self.shop.description)
class ShopQueryViewTests(TestCase):
    def setUp(self):
        self.shop1 = Shop.objects.create(name='Shop 1', address='Address 1', contact='Contact 1', description='Description 1', latitude=1.0, longitude=1.0)
        self.shop2 = Shop.objects.create(name='Shop 2', address='Address 2', contact='Contact 2', description='Description 2', latitude=2.0, longitude=2.0)
        self.shop3 = Shop.objects.create(name='Shop 3', address='Address 3', contact='Contact 3', description='Description 3', latitude=3.0, longitude=3.0)

    def test_shop_query_results(self):
        response = self.client.post(reverse('shop_query'), {
            'latitude': 0.0,
            'longitude': 0.0,
            'distance': 2.0
        })

        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertTemplateUsed(response, 'shop_query_results.html')  # Check if the correct template is used

        self.assertContains(response, self.shop1.name)  # Check if shop 1 is in the response
        self.assertNotContains(response, self.shop2.name)  # Check if shop 2 is not in the response
        self.assertNotContains(response, self.shop3.name)  # Check if shop 3 is not in the response

    def test_shop_query_results_no_shops(self):
        response = self.client.post(reverse('shop_query'), {
            'latitude': 10.0,
            'longitude': 10.0,
            'distance': 2.0
        })

        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertTemplateUsed(response, 'shop_query_results.html')  # Check if the correct template is used

        self.assertNotContains(response, self.shop1.name)  # Check if shop 1 is not in the response
        self.assertNotContains(response, self.shop2.name)  # Check if shop 2 is not in the response
        self.assertNotContains(response, self.shop3.name)  # Check if shop 3 is not in the response

    def test_shop_query_view_get(self):
        response = self.client.get(reverse('shop_query'))

        self.assertEqual(response.status_code, 200)  # Check if the view returns a successful response
        self.assertTemplateUsed(response, 'shop_query.html')  # Check if the correct template is used


