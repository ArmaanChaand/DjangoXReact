from django.db import models
from User.models import CustomUser

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    body  = models.TextField(max_length=500, blank=False, null=False)
    maker = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, null=True, related_name="my_notes")