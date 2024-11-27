from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListDebtsView.as_view(), name='CreateListDebtsView'),
    path('<int:id>', views.DetailUpdateDeleteDebtsView.as_view(), name='CreateListDebtsView'),
    path('lenders', views.CreateListLendersView.as_view(), name='CreateListDebtsView'),
    path('lenders/<int:id>', views.DetailUpdateDeleteLendersView.as_view(), name='CreateListDebtsView'),
]
