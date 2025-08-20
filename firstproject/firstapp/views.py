from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm
# Create your views here.

def hello_world(request):
    '''
    This is function based view which is taking a request as a parameter here'''
    return HttpResponse("Hello world!")


class HelloEthiopia(View):
    '''
    THis is class base view, having get()'''
    def get(self, request):
        return HttpResponse("Hello Ethiopia")
    

def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Success")

    return render(request, 'index.html', {'form': form})

