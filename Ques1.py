# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from time import sleep

@receiver(post_save, sender=YourModel)
def my_handler(sender, instance, created, **kwargs):
    sleep(5)  # Simulate a delay
    print("Signal Handled!")

# views.py
from django.shortcuts import render
from .models import YourModel

def trigger_signal(request):
    YourModel.objects.create(name="Test")  # This triggers the signal
    return render(request, "some_template.html")
