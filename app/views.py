from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Pageresponse(request):
    return render(request,'res.html')

def HtResponse(request):
    return HttpResponse('<h1>HIiii</h1>')