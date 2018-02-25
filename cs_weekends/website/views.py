from django.shortcuts import render

from .models import Session, Announcement, About, Compendia, Supplementary

def default(request):
    return render(request, "base.html")


