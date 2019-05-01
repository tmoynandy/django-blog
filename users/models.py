from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model) :
    #if user is deleted, profile is deleted as well
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        str=self.user.username
        return str+' Profile'

    ##for resizing image - we create a custom save function, over parent save()
    def save(self, *args, **kwargs):
        ##running save parent class
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300 :
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



