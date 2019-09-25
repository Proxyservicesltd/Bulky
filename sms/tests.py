from django.test import TestCase
from  .models import BulkNumbers

# Create your tests here.
class BulkNumberTest(TestCase):

    def setUp(self):
        self.number1 = BulkNumbers.objects.create(
            name='Dennis',
            phone_number=+254897423324
        )

    def test_project_is_assigned_slug_on_creation(self):
        self.assertEquals(self.number1)