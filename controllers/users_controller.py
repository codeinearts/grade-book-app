from flask import request, redirect, url_for, Blueprint, render_template

from services.users_service import Service

users_bp = Blueprint("users", __name__)
service = Service()

@users_bp.route('/users', methods=['GET'])
def read():
    return service.read()

@users_bp.route('/users/create', methods=['POST'])
def create():
    # Recoger los datos del formulario
    rut = request.form['rut']
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    return service.create()
