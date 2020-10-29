""" Users app """

# Django
from django.apps import AppConfig


class UsersConfig(AppConfig):
    """ Name users config. """
    name = 'users'

    def ready(self):
        import users.signals
