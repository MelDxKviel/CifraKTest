# CifraKTest

## Functional

- CRUD types of news
- CRUD news
- Possibility to get a list types of news
- Possibility to get a list news
- Possibility to get a list of news by a type

# Instructions

## Clone repository

```
git clone https://github.com/MelDxKviel/CifraKTest.git
```
```
cd CifraKTest
```
 
## Build and run docker-compose

```
docker-compose up --build
```

## Make migrations

```
docker-compose exec server python manage.py makemigraions
```
```
docker-compose exec server python manage.py migrate
```

## API Documentation

You can find API docs on http://0.0.0.0:8000/api/schema/
