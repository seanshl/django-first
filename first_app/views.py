from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Each View create at least one variable
def index(request):
    """
    type: request
    """
    return HttpResponse("Hello World!")

