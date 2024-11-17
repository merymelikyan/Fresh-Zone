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

