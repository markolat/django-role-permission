from django.core.management.base import BaseCommand, CommandError

from .models import Role, Permission


class Command(BaseCommand):
    help = 'Initial Role and Permission tables seeder'

    def handle(self, *args, **options):
        
        # Roles
        Role.objects.bulk_create(
            [
                Role(name="root"),
                Role(name="admin"),
                Role(name="owner"),
                Role(name="user"),
            ]
        )

        self.stdout.write(self.style.SUCCESS('Roles seeded'))

        # Permissions
        Permission.objects.bulk_create(
            [
                Permission(name="create"),
                Permission(name="read"),
                Permission(name="update"),
                Permission(name="delete")
            ]
        )

        self.stdout.write(self.style.SUCCESS('Permissions seeded'))

        # Role_permissions
        ThroughModel = Role.permissions.through

        roles = Role.objects.all()
        permissions = Permission.objects.all()
        
        ThroughModel.objects.bulk_create(
            [
                ThroughModel(role_id=roles[0].pk, permission_id=permissions[0].pk),
                ThroughModel(role_id=roles[0].pk, permission_id=permissions[1].pk),
                ThroughModel(role_id=roles[0].pk, permission_id=permissions[2].pk),
                ThroughModel(role_id=roles[0].pk, permission_id=permissions[3].pk),
                ThroughModel(role_id=roles[1].pk, permission_id=permissions[0].pk),
                ThroughModel(role_id=roles[1].pk, permission_id=permissions[1].pk),
                ThroughModel(role_id=roles[1].pk, permission_id=permissions[2].pk),
                ThroughModel(role_id=roles[1].pk, permission_id=permissions[3].pk),
                ThroughModel(role_id=roles[2].pk, permission_id=permissions[1].pk),
                ThroughModel(role_id=roles[2].pk, permission_id=permissions[2].pk),
                ThroughModel(role_id=roles[3].pk, permission_id=permissions[1].pk),
            ]
        )

        self.stdout.write(self.style.SUCCESS('Role_permission seeded'))