from django.test import TestCase
from geo_app.forms import PlaceForm
from geo_app.models import Place
from django.contrib.auth.models import User


class TestForms(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='test',
            password='111',
            is_active=True,
            is_staff=True,
            is_superuser=True
            )

    def test_place_form_valid_data(self):
        form = PlaceForm(data={
            'name': 'Test',
            'geom': '{"type":"Point","coordinates":[70.123456,70.123456]}',
            'comment': 'info'
            })

        self.assertTrue(form.is_valid())

    def test_place_form_no_data(self):

        form = PlaceForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_place_form_save_data(self):

        form = PlaceForm(data={
            'name': 'Test',
            'geom': '{"type":"Point","coordinates":[70.123456,70.123456]}',
            'comment': 'info'
            })
        form.is_valid()
        form.save(self.user)

        self.assertEquals(Place.objects.first().name, 'Test')
        self.assertEquals(
            Place.objects.first().location.json,
            '{ "type": "Point", "coordinates": [ 70.123456, 70.123456 ] }'
        )
        self.assertEquals(Place.objects.first().comment, 'info')
