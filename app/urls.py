from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path("", views.index, name = "index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('blog_post/', views.blog_post, name="blog_post"),
    path('portfolio/', views.portfolio, name="portfolio"),
          path('gallery/<int:gallery_blocks_id>', 
          views.gallery_block, name="gallery_blocks"),     
           
] 