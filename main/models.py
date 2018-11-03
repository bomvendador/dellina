from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class CompanyInfo(models.Model):
    main_tel = models.CharField(max_length=20, null=True, blank=True)
    main_email = models.CharField(max_length=20, null=True, blank=True)


class Role(models.Model):
    name = models.CharField(max_length=20)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_fio = models.CharField(max_length=20, null=True, blank=True)
    user_tel = models.CharField(max_length=20, null=True, blank=True)
    user_email = models.CharField(max_length=20, null=True, blank=True)
    user_login = models.CharField(max_length=20, null=True, blank=True)
    user_notes = models.CharField(max_length=100, null=True, blank=True)


class PortfolioItem(models.Model):
    name = models.CharField(max_length=2000, null=True, blank=True)
    short_name = models.CharField(max_length=200, null=True, blank=True)
    client = models.CharField(max_length=200, null=True, blank=True)
    period = models.CharField(max_length=200, null=True, blank=True)
    sum = models.CharField(max_length=20, null=True, blank=True)
    vol = models.CharField(max_length=20, null=True, blank=True)
    main_image = models.CharField(max_length=200, null=True, blank=True)


class PortfolioItemImages(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    item = models.ForeignKey(PortfolioItem, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)


class PortfolioItemImagesSmall(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    item = models.ForeignKey(PortfolioItem, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)


class PortfolioItemImagesBig(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    item = models.ForeignKey(PortfolioItem, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio/', null=True, blank=True)

