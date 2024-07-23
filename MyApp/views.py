from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "MyApp/index.html", {})


def pricing(request):
    return render(request, "MyApp/pricing.html", {})

def portfolio(request):
    return render(request, "MyApp/portfolio.html", {})

def card1(request):
    return render(request, "MyApp/card1.html", {})


def card3(request):
    return render(request, "MyApp/card3.html", {})

def card6(request):
    return render(request, "MyApp/card6.html", {})