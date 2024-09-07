from django.urls import path
from . import views

urlpatterns = [
    path('api/countries', views.countries_list),
    path('api/countries/<int:pk>', views.countries_detail)
]