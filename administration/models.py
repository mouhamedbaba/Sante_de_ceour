from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Site(models.Model):

    name = models.CharField(max_length=50)
    logo = models.FileField(upload_to='site/')
    avatar = models.ImageField(upload_to='site/')
    favicon = models.FileField(upload_to='Site/')
    
    

    class Meta:
        verbose_name = ("site")
        verbose_name_plural = ("sites")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



class Collect(models.Model):

    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='collects/')
    description = models.TextField()
    by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    post_at = models.DateField()
    goal = models.DecimalField(max_digits=10, decimal_places=0)
    raised = models.DecimalField(max_digits=10, decimal_places=0, default= 0)
    end_date = models.DateTimeField(null=True)
    confirmer = models.BooleanField(default=False)
    posted = models.BooleanField(default=False)
    is_amount_reached = models.BooleanField(default= False)
                                      
    
    class Meta:
        verbose_name = ("Collect")
        verbose_name_plural = ("Collects")

    def __str__(self):
        return self.title


