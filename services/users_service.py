from repositories.users_repository import Repository
from flask import render_template
from utils.commons.users_data_models import User


in_construction: str = "in-construction.html"

class Service:
    def __init__(self):
        self.repository = Repository()

    def create(self, user: User) -> str:

        self.repository.create(user)


        # Validar los campos básicos
        # if not rut or not name or not lastname or not email:
            # return "<h1>Faltan datos. Por favor, rellena todos los campos.</h1>"


    def read(self) -> str:
        return render_template(in_construction)
