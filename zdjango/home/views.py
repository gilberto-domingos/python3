from zdjango.shortcuts import render
from zdjango.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "home.pgs")

