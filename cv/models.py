from django.db import models
from pyuploadcare.dj.models import ImageField
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    """
    Project class that defines objects of the projects built
    """
    project_name = models.CharField(max_length=255, null=True, blank=True)
    project_url = models.URLField(max_length=100, null=True, blank=True)
    project_code = models.URLField(max_length=100)
    # project_screenshot = models.ImageField(upload_to='screenshots/', blank=True, null=True)
    project_screenshot = ImageField(blank=True, manual_crop="800x800")
    project_description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.project_name)

class Cv(models.Model):
    """
    Cv class that defines objects of the cv 
    """
    cv_body = HTMLField()
    cv_name = models.CharField(max_length= 250, null=False)

    def __str__(self):
        return str(self.cv_name)

class Technique(models.Model):
    """
    Class that  defines my techniques
    """
    technique_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.technique_name)


class Info(models.Model):
    """
    Class that defines my information
    """
    my_name = models.CharField(max_length=100, null=True, blank=True)
    my_title = models.CharField(max_length=250, null=True, blank=True)
    my_github = models.CharField(max_length=80, null=True, blank=True)
    my_linkedin = models.CharField(max_length=80, null=True, blank=True)
    my_email = models.EmailField()
    # my_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
    my_image = ImageField(blank=True, manual_crop="800x800")
    pub_date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return str(self.my_title)
