from django.urls import path
from . import views

app_name = "arrays"

urlpatterns = [
    path('', views.arrays_view, name='arrays_list'),
]
