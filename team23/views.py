from django.views import View
from django.shortcuts import render


def about(request):
    context = {
        "title": "About"
    }
    return render(request,"about.html",context)