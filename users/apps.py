from django.apps import AppConfig


# noinspection PyUnresolvedReferences
class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        import users.signals
