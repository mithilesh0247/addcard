from django.shortcuts import render, redirect

# Create your views here.

from testapp.forms import CardRegistration
from testapp.models import Card

from django.http import HttpResponseRedirect


def add_card(request):
    if request.method == 'POST':
        fm = CardRegistration(request.POST)
        if fm.is_valid():
            im = fm.cleaned_data['image']
            tl = fm.cleaned_data['title']
            desc = fm.cleaned_data['description']
            reg = Card(image=im, title=tl, description=desc)
            reg.save()
            return redirect('/')
            fm = CardRegistration()
    else:
        fm = CardRegistration()
    stud = Card.objects.all()
    return render(request, 'add.html', {'form': fm})


def update_data(request, id):
    if request.method == 'POST':
        pi = Card.objects.get(pk=id)
        fm = CardRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('/')
    else:
        pi = Card.objects.get(pk=id)
        fm = CardRegistration(request.POST, instance=pi)
    return render(request, 'update.html', {'form': fm})


def home(request):
    cards = Card.objects.all()
    for card in cards:
        print(card.image)
    return render(request, 'home.html', {"cards": cards})
