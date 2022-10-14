from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def projects(request):
    return render(request, 'projects.html')
def aboutme(request):
    return render(request, 'aboutme.html')
def contact(request):
    return render(request, 'contact.html')