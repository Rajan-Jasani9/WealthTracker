from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListAssetsView.as_view(), name='CreateListAssetsView'),
    path('<int:id>', views.DetailUpdateDeleteAssetsView.as_view(), name='CreateListAssetsView'),
]
