# services/user_service.py
from repositories.repository import Repository
from flask import render_template


class Service:
    def __init__(self):
        self.repository = Repository()

    def home(self,):
        # HTML de bienvenida para el home
        return render_template("users.html")

    def create_user(self, user_id, user_data):
        return self.repository.save(user_id, user_data)

    def delete_user(self, user_id):
        return self.repository.delete(user_id)
