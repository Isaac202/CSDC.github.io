from django.db.models.expressions import F
from django.shortcuts import render
from base.models import Home

def home(request):
    home = Home.objects.all()
    return render(request,'home.html', {'home':home})

def contact(request):
    return render(request,'contact.html')

def awards(request):
    return render(request,'awards.html')

def venue(request):
    return render(request,'venue.html')

def conference_schedule(request):
    return render(request,'conference_schedule.html')

def registrationcsds(request):
    return render(request,'registrationcsds.html')

def call_papers(request):
    return render(request,'call_papers.html')

def soic_special_issue(request):
    return render(request,'soic_special_issue.html')

def committees(request):
    return render(request,'committees.html')

def keynotespeakers(request):
    return render(request,'keynotespeakers.html')

def short_courses(request):
    return render(request,'short_courses.html')

def local(request):
    return render(request,'local.html')


def ips_round_tables(request):
    return render(request,'ips_round_tables.html')

def registercsds(request):
    return render(request,'registercsds.html')




