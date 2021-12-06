from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    print("____________________________")
    print("log in")
    ip = request.META.get('REMOTE_ADDR')
    print(" ip: ",ip)
    request.session['ip'] = ip