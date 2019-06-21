from django.shortcuts import render
from .models import Wish
from django.views.generic.edit import CreateView, DeleteView

# Create your views here.

def home(request):
    wishes = Wish.objects.all()
    return render(request, 'home.html', {'wishes': wishes})

class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    template_name = 'add.html'
    success_url = '/'

class WishDelete(DeleteView):
    model = Wish
    success_url = '/'