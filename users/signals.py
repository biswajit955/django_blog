from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

# this is for ip address
@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("____________________________")
    print("log in")
    ip = request.META.get('REMOTE_ADDR')
    print(" ip: ",ip)
    request.session['ip']=ip