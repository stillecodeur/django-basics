import uuid

from django.db import models

# Create your models here.

class User(models.Model):
    id=models.UUIDField(max_length=36,primary_key=True,default=uuid.uuid4(),editable=False)
    name=models.CharField(max_length=100,blank=True,default='')
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=False,null=True)
    status=models.BooleanField(default=True)

    class Meta:
        ordering=('name',)

