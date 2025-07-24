# 📝 SnipBox – Short Notes API with Django REST & JWT

SnipBox is a simple backend API for saving short text snippets with tags, built using **Django REST Framework**, **JWT Authentication**, and **PostgreSQL**. It supports CRUD operations for snippets, tag grouping, and user-based access control.

---

## 🚀 Features

- JWT authentication (`/api/token/`)
- Create/update/delete snippets
- Group snippets with reusable tags
- Filter snippets per user
- PostgreSQL support via Docker
- Fully containerized with Docker Compose

---


## 1. 📦 Clone the Repository

```bash
git clone https://github.com/AbilashEnfield/snipbox.git
cd snipbox
```

## 2. 📦 Create env

Create a .env file in the root directory

```
snipbox/
├── snippets/           # App for snippet logic
├── snipbox/            # Main Django project
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── README.md

```
with following contents
```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=database
DB_USER=user
DB_PASSWORD=password
DB_HOST=db
DB_PORT=5432
```

## 3. 🐳 Start App with Docker

1. Build the containers - ```docker-compose build```
2. Up the containers - ```docker-compose up```
3. Create the migrations - ```docker-compose run web python manage.py makemigrations```
4. Migrate - ```docker-compose run web python manage.py migrate```
5. Create Superuser - ```docker-compose run web python manage.py createsuperuser```

## 4. Testing

kindly use the attached postman collection and start testing

