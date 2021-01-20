from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    #getting/creating an instance of the model we want to add info to/about we use OneToOneField()
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    #additional info we want to add
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username