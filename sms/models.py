from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class BulkNumbers(models.Model):
    name = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    
    
    

    class Meta:
        verbose_name = _("")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
)
