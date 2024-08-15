# Temario

- Contenerdores y Docker: API y DB
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

# Docker commands

Build docker image -> `docker build . -t grade-book-app-image`

Run docker image in a container -> `docker run --name grade-book-app-container grade-book-app-image`

Run docker image in a container with interactive tty -> `docker run -i -t --name grade-book-app-container-terminal grade-book-app-image /bin/bash`

Attach shell to container -> `docker exec -it grade-book-app-container-terminal bash`

Start container with attached STDIN/STDERR  -> `docker start -a -i grade-book-app-container`

Stop container -> `docker stop grade-book-app-container`

Delete container -> `docker rm grade-book-app-container`
