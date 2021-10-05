from django.test import TestCase, Client
from django.urls import reverse
from geo_app.models import Place
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class TestViewsWhenUserIsAuthorized(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='test',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )
        self.user.set_password('111')
        self.user.save()
        self.user = authenticate(username='test', password='111')
        login = self.client.login(username='test', password='111')

        self.places_url = reverse('places')
        self.create_place_url = reverse('create_place')

    def test_places_GET(self):
        response = self.client.get(self.places_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'geo_app/places.html')

    def test_create_place_GET(self):
        response = self.client.get(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'geo_app/place_create_form.html')

    def test_create_place_POST_adds_new_place(self):
        response = self.client.post(self.create_place_url, {
            'name': ['test'],
            'geom': ['{"type":"Point","coordinates":[70.000000,70.000000]}'],
            'comment': ['info']
        })

        self.assertEquals(response.status_code, 301)
        self.assertEquals(Place.objects.first().name, 'test')

    def test_create_place_POST_no_data(self):
        response = self.client.post(self.create_place_url)

        self.assertEquals(response.status_code, 200)
        self.assertEquals(Place.objects.count(), 0)


class TestViewsWhenUserIsNotAuthorized(TestCase):

    def setUp(self):
        self.client = Client()

        self.places_url = reverse('places')
        self.create_place_url = reverse('create_place')

    def test_places_GET(self):
        response = self.client.get(self.places_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_GET(self):
        response = self.client.get(self.create_place_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_POST_adds_new_place(self):
        response = self.client.post(self.create_place_url, {
            'name': ['test'],
            'geom': ['{"type":"Point","coordinates":[70.123456,70.123456]}'],
            'comment': ['info']
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)

    def test_create_place_POST_no_data(self):
        response = self.client.post(self.create_place_url)

        self.assertEquals(response.status_code, 302)
        self.assertEquals(response.context, None)
