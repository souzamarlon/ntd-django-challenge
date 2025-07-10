Django API Challenge

A simple Django REST API to load planet data from the GraphQL API, store it in a database, and expose full CRUD endpoints.

🚀 Features

Fetch planet data from SWAPI GraphQL

Store data in a Django model with climates, terrains, population, and name

RESTful API with full CRUD via Django REST Framework

SQLite database (for simplicity)

Docker support for quick setup

Custom management command to load planet data

🐳 Getting Started with Docker

1. Clone the repository

git clone https://github.com/your-username/ntd-django-challenge.git
cd ntd-django-challenge/django_api

2. Build and start the containers

docker compose up --build -d

3. Apply migrations, create superuser, and load planets

You can run all setup steps with a single command using the Makefile:

make install

This will:

Apply database migrations

Prompt you to create a superuser

Import planet data from SWAPI

4. Access the app

API Root: http://localhost:8000/planets/

Admin Panel: http://localhost:8000/admin/

🧪 Running Tests

docker compose run --rm web pytest

🤖 API Endpoints

Example endpoint:

GET /planets/planet/
POST /planets/planet/
PUT /planets/planet/<id>/
DELETE /planets/planet/<id>/

📬 Contact

Built by Marlon — feel free to reach out for questions or feedback.
