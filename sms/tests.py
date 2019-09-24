from django.test import TestCase
from  .models import BulkNumbers

# Create your tests here.
class BulkNumberTest(TestCase):
    def create_number(self):
        self.assertEqual(str(name),str(phone_number))