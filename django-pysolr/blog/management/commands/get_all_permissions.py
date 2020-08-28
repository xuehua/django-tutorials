# The codes is modified based on a code from the following link.
# https://timonweb.com/django/how-to-get-a-list-of-all-user-permissions-available-in-django-based-project/

from django.contrib import auth
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission


# From https://stackoverflow.com/questions/16573174/how-to-get-user-permissions
def get_user_permissions(user):
    if user.is_superuser:
        return Permission.objects.all()
    return user.user_permissions.all() | Permission.objects.filter(group__user=user)

class Command(BaseCommand):
    help = 'Get a list of all permissions available in the system.'

    def add_arguments(self, parser):
        parser.add_argument('--user', dest='username', type=str)

    def handle(self, *args, **options):
        permissions = set()
        
        # We create (but not persist) a temporary superuser and use it to game the
        # system and pull all permissions easily.
        # tmp_superuser = get_user_model()(
        #     is_active=True,
        #     is_superuser=True
        # )
        username = options['username']

        tmp_superuser = get_user_model().objects.get(username=username)
        # We go over each AUTHENTICATION_BACKEND and try to fetch
        # a list of permissions
        for backend in auth.get_backends():
            if hasattr(backend, "get_all_permissions"):
                permissions.update(backend.get_all_permissions(tmp_superuser))

        # Make an unique list of permissions sorted by permission name.
        sorted_list_of_permissions = sorted(list(permissions))

        # Send a joined list of permissions to a command-line output.
        self.stdout.write('\n'.join(sorted_list_of_permissions))

        print("---- Use get_user_permissions:")
        permissions=get_user_permissions(tmp_superuser)
        for permission in permissions: 
            #print(permission.content_type, permission.codename)
            print(permission.content_type.app_label + "." + permission.codename)

