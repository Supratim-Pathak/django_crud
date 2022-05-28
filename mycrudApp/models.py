from pyexpat import model
from unicodedata import name
from django.db import models

# Create your models here.
class stu_info(models.Model):
    stu_name = models.CharField(max_length=50)
    mobile_no = models.BigIntegerField()
    age = models.IntegerField()
    createated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)