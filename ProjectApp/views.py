from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'Home.html')

def About(request):
    return render(request, 'About.html')