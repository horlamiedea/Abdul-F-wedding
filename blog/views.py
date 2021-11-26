from django.shortcuts import render

# Create your views here.


def homeview(request):
    return render(request, 'base.html')


def couple(request):
    return render(request, 'couple.html')


def schedule(request):
    return render(request, 'schedule.html')


def rsvp(request):
    return render(request, 'rsvp.html')


def travel(request):
    return render(request, 'travel.html')


def faq(request):
    return render(request, 'faq.html')
