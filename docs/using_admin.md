# Using admin

For using the admin site, you will need to create a super user.

Run the `createsuperuser` management command:

    docker exec -it myproject_web_1 python manage.py createsuperuser

Now you can log in to the admin site:

http://127.0.0.1:8000/admin/
