from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model) :
    #if user is deleted, profile is deleted as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        str=self.user.username
        return str+' Profile'


