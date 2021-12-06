from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile



class Post(models.Model):
    title = models.CharField(max_length=100,help_text="enter within 100 charecter")
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    # this is for show demo form admin site (if you use this than genarate a button for demo )
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})

    