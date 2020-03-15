from django.test import TestCase
from .models import NatParks


class NatParksModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        NatParks.objects.create(title='first natpark')
        NatParks.objects.create(description='a description here')

    def test_title_content(self):
        natpark = NatParks.objects.get(id=1)
        expected_object_name = f'{natpark.title}'
        self.assertEquals(expected_object_name, 'first natpark')

    def test_description_content(self):
        natpark = NatParks.objects.get(id=2)
        expected_object_name = f'{natpark.description}'
        self.assertEquals(expected_object_name, 'a description here')