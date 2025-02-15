from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import transaction

@receiver(post_save, sender=YourModel)
def my_handler(sender, instance, created, **kwargs):
    print(f"Is the signal in the same transaction? {transaction.get_autocommit()}")

# views.py
from django.shortcuts import render
from .models import YourModel
from django.db import transaction

def trigger_signal(request):
    with transaction.atomic():  # Start a transaction block
        YourModel.objects.create(name="Test")  # This triggers the signal
        print(f"Is the view in a transaction? {transaction.get_autocommit()}")
    return render(request, "some_template.html")
