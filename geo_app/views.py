from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Place
from .forms import PlaceForm


class PlaceDetail(LoginRequiredMixin, ListView):
    template_name = 'geo_app/place.html'
    context_object_name = 'place'

    def get_queryset(self):
        return Place.objects.get(id=self.kwargs['id'])


class PlaceShow(LoginRequiredMixin, ListView):
    template_name = 'geo_app/places.html'
    context_object_name = 'user_places'

    def get_queryset(self):
        return Place.objects.filter(author=self.request.user)


class PlaceCreate(LoginRequiredMixin, View):
    def get(self, request):
        place_form = PlaceForm()

        return render(
            request, 
            'geo_app/place_create_form.html',
            context={'place_form': place_form})

    def post(self, request):
        bound_place_form = PlaceForm(request.POST)
        user = request.user

        if bound_place_form.is_valid():
            bound_place_form.save(user)

            return redirect('/places/', permanent=True)
        return render(
            request, 
            'geo_app/place_create_form.html',
            context={'place_form': bound_place_form})
