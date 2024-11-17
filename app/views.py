from django.shortcuts import render

from .models import (
    HeaderText,
    FooterText,
    Sliders,
    SliderImages,
    ResentPost1,
    ResentPost2,
    Post2List,
    FoodGalleryMain,
    FoodGallery,
    About,
    WebDesign,
    TestimonialsMain,
    Testimonials

    
    )


def index(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "sliders": Sliders.objects.all(),
        "slider_images": SliderImages.objects.all(),
        "resent_post1": ResentPost1.objects.all().first(),
        "resent_post2": ResentPost2.objects.all().first(),
        "post2_list": Post2List.objects.all(),
        "food_gallery_main": FoodGalleryMain.objects.all().first(),
        "food_gallery": FoodGallery.objects.all(),
       
   }
    
    return render(request,"home.html", context)

def about(request):
    context = {
        "header_text": HeaderText.objects.all().first(),
        "footer_text": FooterText.objects.all().first(),
        "about": About.objects.all().first(),
        "web_design": WebDesign.objects.all().first(),
        "testimonials_main": TestimonialsMain.objects.all().first(),
        "testimonials": Testimonials.objects.all(),
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