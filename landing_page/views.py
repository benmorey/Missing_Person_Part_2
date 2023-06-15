from django.shortcuts import render
from django.http import HttpResponse
from .models import MissingPersons

# Create your views here.
def landingPageView(request):
    return render(request, 'landing_page/index.html')

def tableView(request):
    data = MissingPersons.objects.all()
    context = {
        "the_missing" : data
    }
    return render(request, 'landing_page/table.html', context)