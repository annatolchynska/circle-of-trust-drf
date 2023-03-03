from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# partially used the code from DRF-API walkthrough


class Profile(models.Model):
    '''Profile model'''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_xt3gli',
    )
    bio = models.TextField()

    class Meta:
        ''' displays the newest profile '''
        ordering = ['-created_on']

    def __str__(self):
        ''' shows what to display '''
        return f"{self.owner}'s profile."


# function taken from DRF-API walkthrough
def create_profile(sender, instance, created, **kwargs):
    ''' make sure the profile is created every time the User is created '''
    if created:
        Profile.objects.create(owner=instance)


post_save.connect(create_profile, sender=User)
