import imp
import re
from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.signals import user_logged_in, user_signed_up

User = get_user_model()

def user_logged_in_reciever(request, user, **kwargs):
    # print(f'{request} logged in request')
    # print(user)
    pass

user_logged_in.connect(user_logged_in_reciever, sender=User)

def user_signed_up_reciever(request, user, **kwargs):
    # print(f'{request} signed up request')
    # print(user)
    pass

user_signed_up.connect(user_signed_up_reciever, sender=User)

class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='subscriber')
    profile_picture = models.ImageField(upload_to='profile_pic', 
                        blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username