from django.shortcuts import render
from rest_framework.generics import GenericAPIView
# Create your views here.
class CreateListExpensesView(GenericAPIView):

     def post(self, request):
          pass

     def get(self, request):
          pass


class DetailUpdateDeleteExpensesView(GenericAPIView):

     def patch(self, request, id):
          pass
     
     def get(self, request, id):
          pass

     def delete(self, request, id):
          pass
     