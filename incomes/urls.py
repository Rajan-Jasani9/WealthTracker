from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListIncomesView.as_view(), name='CreateListDebtsView'),
    path('<int:id>', views.DetailUpdateDeleteIncomesView.as_view(), name='CreateListDebtsView'),
]
