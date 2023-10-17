from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User,Group
from .models import Profile

#Hna fax kandiro register kayzido mobaxaratan f group client 
@receiver(post_save, sender=User)
def my_callback(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='client')
        instance.groups.add(group)
        Profile.objects.create(user = instance,name=instance.username)
        print("New instance created!")



