from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Client

@receiver(post_save, sender=User)
def ensure_client_for_superuser(sender, instance, created, **kwargs):
    if created and instance.is_superuser:  # Check if the user is a superuser
        if not hasattr(instance, 'client'):  # Ensure the superuser has a Client
            Client.objects.create(
                user=instance,
                email=instance.email,  # Use the superuser's email
                name=instance.username  # Use the superuser's username as the name
            )
    if instance.is_superuser and instance.username != instance.email:  # Ensure username matches email
        instance.username = instance.email
        # Prevent recursion by disconnecting the signal temporarily
        post_save.disconnect(ensure_client_for_superuser, sender=User)
        instance.save()
        post_save.connect(ensure_client_for_superuser, sender=User)
