from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.CreateListExpensesView.as_view(), name='CreateListDebtsView'),
    path('<int:id>', views.DetailUpdateDeleteExpensesView.as_view(), name='CreateListDebtsView'),
]
