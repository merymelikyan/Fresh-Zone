from django.db import models


class HeaderText(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Header Text"
        verbose_name_plural = "Header Texts"

 
class FooterText(models.Model):
    text = models.CharField(max_length=255)
    link_url = models.URLField(max_length=255)
    link_name = models.CharField(max_length=255)
 


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Footer Text"
        verbose_name_plural = "Footer Text"


class Sliders(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
   
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Sliders"
        verbose_name_plural = "Sliders"



class SliderImages(models.Model):
    image_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="slider_images")
   
 
    def __str__(self):
        return f"{self.image_title}"
    
    class Meta:
        verbose_name = "Slider Images"
        verbose_name_plural = "Slider Images"


class ResentPost1(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
    description3 = models.CharField(max_length=1500, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_class = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="resent_post1", blank=True, null=True)
    link_url1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Resent Post1"
        verbose_name_plural = "Resent Post1"



class ResentPost2(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Resent Post2"
        verbose_name_plural = "Resent Post2"



class Post2List(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Post2 List"
        verbose_name_plural = "Post2 List"


class FoodGalleryMain(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Food Gallery Main"
        verbose_name_plural = "Food Gallery Main"



class FoodGallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="food_gallery")
   
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Food Gallery"
        verbose_name_plural = "Food Gallery"



class About(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="about")
   
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"


class WebDesign(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=500, blank=True, null=True)
    description2 = models.CharField(max_length=500, blank=True, null=True)
    description3 = models.CharField(max_length=500, blank=True, null=True)
    description4 = models.CharField(max_length=2500, blank=True, null=True)
    description5 = models.CharField(max_length=2500, blank=True, null=True)
    image_title = models.CharField(max_length=255, blank=True, null=True)
    image_class = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to="web_desine", blank=True, null=True)
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_url3 = models.CharField(max_length=255, blank=True, null=True)
    link_url4 = models.URLField(max_length=255, blank=True, null=True)
    link_url5 = models.URLField(max_length=255, blank=True, null=True)
    link_url6 = models.CharField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    link_name3 = models.CharField(max_length=255, blank=True, null=True)
    link_name4 = models.CharField(max_length=255, blank=True, null=True)
    link_name5 = models.CharField(max_length=255, blank=True, null=True)
    link_name6 = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Web Design"
        verbose_name_plural = "Web Design"


class TestimonialsMain(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Testimonials Main"
        verbose_name_plural = "Testimonials Main"


class Testimonials(models.Model):
    description = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
 
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"



class GalleryMain(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Gallery Main"
        verbose_name_plural = "Gallery Main"


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery")
    link_url = models.URLField(max_length=255)
    link_name = models.CharField(max_length=255)
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Gallery"


class Gallery1(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="gallery")
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    link_url3 = models.URLField(max_length=255, blank=True, null=True)
    link_name3 = models.CharField(max_length=255, blank=True, null=True)
 
 
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Gallery1"
        verbose_name_plural = "Gallery1"       



class Blog1(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog1")
    text = models.CharField(max_length=255)
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog1"
        verbose_name_plural = "Blog1"


class Blogs2(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1500)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blogs2")
    text = models.CharField(max_length=255)
    
 
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blogs2"
        verbose_name_plural = "Blogs2"



class SideBarMain(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Side Bar Main"
        verbose_name_plural = "Side Bar Main"



class Services(models.Model):
    title = models.CharField(max_length=255)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Services"
        verbose_name_plural = "Services"


class PopularPosts(models.Model):
    description = models.CharField(max_length=500)
    link_name = models.CharField(max_length=255)
    link_url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.link_name}"

    class Meta:
        verbose_name = "Popular Posts"
        verbose_name_plural = "Popular Posts"


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description1 = models.CharField(max_length=2500, blank=True, null=True)
    description2 = models.CharField(max_length=2500, blank=True, null=True)
    description3 = models.CharField(max_length=2500, blank=True, null=True)
    description4 = models.CharField(max_length=2500, blank=True, null=True)
    description5 = models.CharField(max_length=2500, blank=True, null=True)
    description6 = models.CharField(max_length=2500, blank=True, null=True)
    description7 = models.CharField(max_length=2500, blank=True, null=True)
    image_title = models.CharField(max_length=255)
    image_class = models.CharField(max_length=255)
    image = models.ImageField(upload_to="blog_post")
    text1 = models.CharField(max_length=255, blank=True, null=True)
    text2 = models.CharField(max_length=255, blank=True, null=True)
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)
    link_url3 = models.CharField(max_length=255, blank=True, null=True)
    link_url4 = models.CharField(max_length=255, blank=True, null=True)
    link_url5 = models.CharField(max_length=255, blank=True, null=True)
    link_name3 = models.CharField(max_length=255, blank=True, null=True)
    link_name4 = models.CharField(max_length=255, blank=True, null=True)
    link_name5 = models.CharField(max_length=255, blank=True, null=True)
   
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Post"


class CommentsMain(models.Model):
    title = models.CharField(max_length=255)
  
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Comments Main"
        verbose_name_plural = "Comments Main"   



class Comments(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    date = models.CharField(max_length=500)
    time = models.CharField(max_length=255)
    image_title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="comments")
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Comments"
        verbose_name_plural = "Comments"


class Contact(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    link_url1 = models.URLField(max_length=255, blank=True, null=True)
    link_url2 = models.URLField(max_length=255, blank=True, null=True)
    link_name1 = models.CharField(max_length=255, blank=True, null=True)
    link_name2 = models.CharField(max_length=255, blank=True, null=True)

   	
    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"


class Location(models.Model):
    tag = models.CharField(max_length=255)
    title = models.CharField(max_length=250)
    description1 = models.CharField(max_length=250, blank=True, null=True)
    description2 = models.CharField(max_length=250, blank=True, null=True)
    description3 = models.CharField(max_length=250, blank=True, null=True)
    phone_number = models.CharField(max_length=255)
    email_text= models.CharField(max_length=255)
    email_url= models.CharField(max_length=255)
   	
    def __str__(self):
        return self.tag
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Location"



