from django.shortcuts import render

# Create your views here.


def index(request):
    """View function to return the index page of the site."""
    return render(request, 'home/index.html')
