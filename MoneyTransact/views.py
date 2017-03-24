from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Balance

def index(request):
    return  HttpResponse("<h1> Your Balance sheet </h1> ")

def detail(request, transaction_id):
    # print( transaction_id)
    all_transactions = Balance.objects.filter
    return  HttpResponse("<h2> Details for all transaction with this " + str(transaction_id) +  " are :   </h2> ")
    # + str(balance_id)+  " are  </h2> ")