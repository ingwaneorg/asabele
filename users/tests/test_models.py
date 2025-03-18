from django.test import TestCase

from django.contrib.auth import get_user_model


class CustomUser(TestCase):

    username = 'will'
    email = 'will@email.org'
    first_name = 'William'
    last_name = 'Fence'
    is_active = True

    def test_create_user(self):
        # Save the user record
        new_user = get_user_model().objects.create_user(
            self.username,
            email=self.email,
            password='password123',
            first_name=self.first_name,
            last_name=self.last_name,
        )
        # Get the user record
        user = get_user_model().objects.get(username=self.username)
        # See that the values are the same
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_superuser, False)  # False for normal user
        self.assertEqual(user.is_staff, False)  # False for normal user


    def test_create_superuser(self):
        # Save the super user record
        new_user = get_user_model().objects.create_superuser(
            self.username,
            email=self.email,
            password='password123',
            first_name=self.first_name,
            last_name=self.last_name,
            
        )
        # Get the user record
        user = get_user_model().objects.get(username=self.username)
        # See that the values are the same
        self.assertEqual(user.username, self.username)
        self.assertEqual(user.email, self.email)
        self.assertEqual(user.first_name, self.first_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.last_name, self.last_name)
        self.assertEqual(user.is_active, True)
        self.assertEqual(user.is_superuser, True)  # True for superuser
        self.assertEqual(user.is_staff, True)  # True for superuser
