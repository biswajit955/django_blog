from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    Gender = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=Gender, default='')
    image = models.ImageField(default='default_male.jpg', upload_to = 'profile_pics')
    

    def __str__(self):
        return f'{self.user.username}  profile.'
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width > 300:
            img.thumbnail( (300,300) )
            img.save(self.image.path)