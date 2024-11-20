from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListDebtsView.as_view(), name='CreateListDebtsView'),
]
