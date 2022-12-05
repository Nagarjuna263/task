from django.shortcuts import render

# Create your views here.
def king(request):
    return render(request,'king.html')