# Temario

- Contenerdores y Docker: API y DB
  - Ways of work: attach shell to container, build docker image, make it work and explore contents
  - Run code within the container
  - Run database container
  - Docker Connectivity
- Workspace setup
  - Virtual environment
  - requirements.txt generation
- Arquitectura Hexagonal: controlador - servicio - repositorio
- API design: Flask Framework
- Test Unitarios
- Swagger
- Deployment: GCP, AWS, Azure

# Extras

- User Interface (Templates or React)
- Autenticación y Autorización
- Continuous Integration & Continuous Delivery

# Key Concepts

- Containers
- Docker
- Docker Compose
- Flask
- Web Application
- Hexagonal Architecture
- Service
- Repository
- Controller
- Unit Test
- Swagger
- JWT

## Docker commands

Build docker image -> `docker build . -t grade-book-app-image`

Run docker image in a container -> `docker run --rm --name grade-book-app-container grade-book-app-image`

Run docker image in a container with interactive tty -> `docker run -it --name grade-book-app-container-terminal grade-book-app-image /bin/bash`

Attach shell to container -> `docker exec -it grade-book-app-container-terminal bash`

Start container with attached STDIN/STDERR -> `docker start -a -i grade-book-app-container`

Stop container -> `docker stop grade-book-app-container`

Delete container -> `docker rm grade-book-app-container`

## Database container

Image documentation can be found at -> https://hub.docker.com/_/postgres

```
docker run --rm -p 5432:5432 --name postgres-database -e POSTGRES_PASSWORD=lagranzanahoriavendra -d postgres
```

## Workspace setup

Python's built-in venv module is the recommended way to create virtual environments. Here's how it works:

### Create the Environment:

```
python3 -m venv my_project_env
```

This command creates a directory named my_project_env containing a copy of the Python interpreter and a set of tools for managing packages.

### Activate the Environment:

#### Linux/macOS:

```
source my_project_env/bin/activate
```

#### Windows:

```
my_project_env\Scripts\activate
```

You'll see the environment name (e.g., (my_project_env)) prepended to your command prompt, indicating that you're now working within the virtual environment.

### Install packages

```
pip install psycopg2
pip install flask
```

### create requirements.txt

```
pip freeze > requirements.txt
```
