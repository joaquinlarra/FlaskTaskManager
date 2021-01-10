# SHELL command queue

This app will run shell commands posted to `v1/tasks/new_task` in background (and enque them). 
You can later check the outpout at `v1/tasks/get_output/:id`.

## Usage

[Install Docker](https://www.docker.com/products/docker-desktop) if you don't have it yet and run the container:

```sh
$ docker-compose up
```
It will run both Web and Mongodb containers on `localhost:5100`.
Swagger runs on `/` so you can test all functions on `http://localhost:5100`

## Stack

- Python 3
- Flask
- Flask-RESTPlus
- Mongoengine
- Docker
- Celery
- Redis
- Swagger

## Structure

```
├── Dockerfile
├── README.md
├── api
│   ├── app.py - Entry point of application
│   ├── config.py - Configuration with environments
│   └── v1 - API version 1
│       ├── database
│       │   └── models.py - All data models app uses
│       └── resources
│           ├── routes.py - List of namespaces for routing
│           └── tasks.py - Example Todo resource
├── docker-compose.yml
├── requirements.txt - Dependencies
```

Made by Joaquín Astelarra