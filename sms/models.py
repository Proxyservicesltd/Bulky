from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class BulkNumbers(models.Model):
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()

    def __str__(self):
        return self.name
    


