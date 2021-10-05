from django.urls import path
from django.views.generic.base import TemplateView
from .views import PlaceShow, PlaceDetail, PlaceCreate


urlpatterns = [
    path('', TemplateView.as_view(template_name='geo_app/index.html')),
    path('place/create/', PlaceCreate.as_view(), name='create_place'),
    path('place/<str:id>/', PlaceDetail.as_view(), name='place_detail_url'),
    path('places/', PlaceShow.as_view(), name='places'),
]
