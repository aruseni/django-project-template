# Django Project Template

This is a minimal Django project template with a custom user model.

To start a project with this template, replace `myproject` with
your project name.

## How to run locally

Clone the repository, open terminal, and add `local_settings.py`:

    ./utils/create_local_settings.py

Then execute the following command:

    docker-compose up

Make sure that you have Docker and docker-compose.

## Execute migrations

Migrations are currently not set to be executed automatically, therefore please
make sure to do it manually using the migrate command:

    docker-compose run web python manage.py migrate
