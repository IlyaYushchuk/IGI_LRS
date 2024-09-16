from django.test import TestCase

from users.models import User
from django.utils import timezone

class UserModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(first_name='Name', last_name='Last name', username='username', phone='+375-99-93-35-123', position='driver')

    def test_phone_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('phone').verbose_name
        self.assertEqual(field_label, 'phone')

    def test_image_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('image').verbose_name
        self.assertEqual(field_label, 'Аватар')
   
    def test_position_label(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('position').verbose_name
        self.assertEqual(field_label, 'position')

    def test_phone_max_length(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('phone').max_length
        self.assertEqual(field_label, 19)

    def test_position_max_length(self):
        user=User.objects.get(id=1)
        field_label = user._meta.get_field('position').max_length
        self.assertEqual(field_label, 150)


    def test_str(self):
        user=User.objects.get(id=1)
        self.assertEqual(str(user), 'username')

