from flask import request, redirect, url_for, Blueprint, render_template
from services.users_service import Service
from utils.commons.postgres_data_models import User

users_bp = Blueprint("users", __name__)
service = Service()

@users_bp.route('/users', methods=['GET'])
def read():
    return service.read()

@users_bp.route('/user/create', methods=['POST'])
def create():
    # Recoger los datos del formulario

    print(request.form)
    print(type(request.form))
    user: User = User(request.form)
    print(user)
    print(type(user))

    service.create(user)
