from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=400)


def user_directory_path(instance, filename): 
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename> 
    return '../data/{0}/{1}'.format(instance.user.username, filename) 

class File(models.Model):
    file_path = models.CharField(max_length=400, null=True, blank=True)
    file_name = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)