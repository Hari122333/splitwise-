from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate , login
from django.views import generic
from django.views.generic import View
from .forms import Userform


# Create your views here.

from django.http import HttpResponse
from .models import Balance

def index(request):
    return  HttpResponse("<h1> Your Balance sheet </h1> ")

def detail(request, transaction_id):
    # print( transaction_id)
    all_transactions =  Balance.objects.filter( taker=str(transaction_id)) \
                        | Balance.objects.filter( Giver=str(transaction_id) )
    print( all_transactions)
    return  HttpResponse("<h2> Details for all transaction with this " + str(transaction_id) +  " are :   </h2> ")
    # + str(balance_id)+  " are  </h2> ")

# def create_new_transaction():

class UserFormView(View):
    form_class = Userform
    template_name = 'MoneyTransact/registration_form.html'

    #blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form' : form} )

    #submitted - process data
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid() :
            user = form.save(commit = False)
            #normalised data

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()

            user=authenticate(username=username , password=password)
            if user is not None :
                if user.is_active :
                    login(request,user)
                    # request.username
                    return redirect('MoneyTransact:index')

        return render(request, self.template_name, {'form' : form} )
