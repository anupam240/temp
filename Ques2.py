import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
import threading

@receiver(post_save, sender=YourModel)
def my_handler(sender, instance, created, **kwargs):
    print(f"Handler is running in thread: {threading.current_thread().name}")

# views.py
from django.shortcuts import render
from .models import YourModel
import threading

def trigger_signal(request):
    print(f"Request is running in thread: {threading.current_thread().name}")
    YourModel.objects.create(name="Test")  # This triggers the signal
    return render(request, "some_template.html")
