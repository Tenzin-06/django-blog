from django.db import models

# Create your models here.
class About(models.Model):
    about_heading = models.CharField(max_length=25)
    about_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.about_heading
    
class SocialLink(models.Model):
    platform_name = models.CharField(max_length=50)
    profile_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.platform_name