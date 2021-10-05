from django.test import SimpleTestCase
from django.urls import reverse, resolve
from geo_app.views import PlaceShow, PlaceCreate


class TestUrls(SimpleTestCase):

    def test_places_url_is_resolves(self):
        url = reverse('places')
        self.assertEquals(resolve(url).func.view_class, PlaceShow)

    def test_create_place_url_is_resolves(self):
        url = reverse('create_place')
        self.assertEquals(resolve(url).func.view_class, PlaceCreate)
