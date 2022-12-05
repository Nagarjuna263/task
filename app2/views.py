from django.shortcuts import render

# Create your views here.
def queen(request):
    return render(request,'queen.html')

def marry(request):
    return render(request,'marry.html')