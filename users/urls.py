from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.UserListView.as_view(), name='CreateListAssetsView'),
    path('login', views.LoginView.as_view(), name='CreateListAssetsView'),
]
