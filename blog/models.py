from django.db import models
from django.utils import timezone
##user is imported from the already created user model that shows in admin
from django.contrib.auth.models import User
#for getting url of a post as a string
from django.urls import reverse

# Create your models here.
#each class will be a table in the db
#each attribute in the class will be a column
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

     ##fetching url of a created post as a string, to be used by view so as to redirect 
    ##on creating a new post - nije kore nebe etuku likhle..chaapless
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    

