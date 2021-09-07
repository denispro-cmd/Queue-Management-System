from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Token(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    department_to_visit = models.CharField(max_length=120)
    purpose = models.TextField()
    address = models.CharField(max_length=120)
    phone = models.CharField(max_length=120)
    token = models.CharField(max_length=9,editable=False)
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return str(self.author)

    def get_absolute_url(self):
        return reverse('token-detail', kwargs={'pk':self.pk})