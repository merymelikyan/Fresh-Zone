from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    
    )


def index(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
       

   }
    
    return render(request,"home.html", context)

def about(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
     
    }
    
    return render(request, "about.html", context)

def contact(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
       
    }
    
    return render(request, "contact.html", context)


def blog(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
       
    }
    
    return render(request, "blog.html", context)



def blog_post(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        
    }
    
    return render(request, "blog_post.html", context)



def portfolio(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
       
    }
    
    return render(request, "portfolio.html", context)