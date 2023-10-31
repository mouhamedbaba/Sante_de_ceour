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
    post_at = models.DateField(blank=True, null=True)
    goal = models.DecimalField(max_digits=10, decimal_places=0)
    raised = models.DecimalField(max_digits=10, decimal_places=0, default= 0)
    end_date = models.DateTimeField(null=True, blank=True)
    confirmer = models.BooleanField(default=False)
    posted = models.BooleanField(default=False)
    is_amount_reached = models.BooleanField(default= False)
                                      
    
    class Meta:
        verbose_name = ("Collect")
        verbose_name_plural = ("Collects")

    def __str__(self):
        return self.title


class BadgeDonneur(models.Model):
    
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Badge de donneur')
        verbose_name_plural = ('Badge de donneurs')

class Donneur(models.Model):

    name = models.CharField(max_length=100, default='anonyme')
    email = models.CharField(max_length=250)
    create_at = models.DateField(auto_now_add=True)
    badges = models.ManyToManyField(BadgeDonneur , blank=True)
    total_don = models.IntegerField(default=0)
    
    def __str__(self):
        """
        Returns a string representation of the object.
        """
        return self.name

    class Meta:
        verbose_name = ('Donneur')
        verbose_name_plural = ('Donneurs')
        
class PayementMethod(models.Model):

    name = models.CharField(max_length=50)
    logo = models.FileField(upload_to='logos', null = True , blank=True)
    usage_number = models.IntegerField(default=0)
    total_amount = models.DecimalField(max_digits=10, decimal_places=0, default=0)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Methode de payement')
        verbose_name_plural = ('Methodes de payement')

class DonCollect(models.Model):
    date = models.DateField(auto_now_add=True)
    collect = models.ForeignKey(Collect, verbose_name=("Collect du don"), on_delete=models.CASCADE)
    donneur = models.ForeignKey(Donneur, on_delete=models.CASCADE)
    amount = models.IntegerField()
    payement_method = models.ForeignKey(PayementMethod, verbose_name=("Methode de payement"), on_delete=models.CASCADE)
    added_by_admin = models.ForeignKey(User, verbose_name=("Ajoute par"), on_delete=models.CASCADE, null = True , blank=True)
    confirmed = models.BooleanField(default=True)
    class Meta:
        verbose_name = ("Don de collect")
        verbose_name_plural = ("Dons de collect")

    def __str__(self):
        return self.collect.title

    def get_absolute_url(self):
        return reverse("DonCollect_detail", kwargs={"pk": self.pk})
