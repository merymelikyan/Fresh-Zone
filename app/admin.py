from django.contrib import admin


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

admin.site.register(HeaderText)
admin.site.register(FooterText)
admin.site.register(Sliders)
admin.site.register(SliderImages)
admin.site.register(ResentPost1)
admin.site.register(ResentPost2)
admin.site.register(Post2List)
admin.site.register(FoodGalleryMain)
admin.site.register(FoodGallery)
admin.site.register(About)
admin.site.register(WebDesign)
admin.site.register(TestimonialsMain)
admin.site.register(Testimonials)
