from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListLiabilitiesView.as_view(), name='CreateListAssetsView'),
]
