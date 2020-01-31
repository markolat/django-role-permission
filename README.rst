=====
Role_Permission
=====

Django reusable app intended to boost development of projects 
which need role-permission logic. 

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "role_permission" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'role_permission',
    ]

2. Run `python manage.py migrate` to create the role-permission models.

3. (OPTIONAL) Run `python manage.py initrolepermission` to seed database with provided 
   default roles and permissions.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create roles and permissions (you'll need the Admin app enabled).

5. Link your User model or any other to Role model.