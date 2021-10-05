from django import forms
from .models import Place
from leaflet.forms.fields import PointField


class PlaceForm(forms.ModelForm):
    geom = PointField(label='Укажите место на карте')

    class Meta:
        model = Place
        fields = ('name', 'geom', 'comment')

    def save(self, user):
        new_place = Place.objects.create(
            name=self.cleaned_data['name'],
            location=self.cleaned_data['geom'],
            comment=self.cleaned_data['comment'],
            author=user
            )
        return new_place
