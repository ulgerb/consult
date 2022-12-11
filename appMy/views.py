from django.shortcuts import render

# Create your views here.

def index(request):
    
    return render(request,'index.html')

def About(request):
    
    return render(request,'about.html')

def Service(request):
    
    return render(request,'service.html')

def Contact(request):
    
    return render(request,'contact.html')

def Detail(request):
    
    return render(request,'detail.html')

# PAGES
def Blog(request):
    
    return render(request,'pages/blog.html')

def Feature(request):
    
    return render(request,'pages/feature.html')

def Team(request):
    
    return render(request,'pages/team.html')

def Testimonial(request):
    
    return render(request,'pages/testimonial.html')