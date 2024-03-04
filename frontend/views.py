from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, "index.html")

def acara(request):
    return render(request, "all_acara.html")
