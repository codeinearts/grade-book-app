from flask import request, redirect, url_for, Blueprint, render_template, jsonify
from services.users_service import Service
from utils.commons.postgres_data_models import User

users_bp = Blueprint("users", __name__)
service = Service()

@users_bp.route("/users", methods=["GET"])
def read():
    return service.read()

@users_bp.route("/echo")
def echo():
    # Insertar en el buscador la siguiente url para testear
    # http://127.0.0.1:5000/echo?echo=echo+this+back+to+me
    to_echo = request.args.get("echo", "")
    response = "{}".format(to_echo)
    return response

@users_bp.route(
        "/user/create",
        methods=["GET", "POST"])
def create():
    try:
        user_data = request.form.to_dict()
        print("Datos del formulario:", user_data)

        if request.method == 'POST':
            # Recoger los datos del formulario
            user: User = User(**user_data)
            print(f"usuario validado: {user}")
            print(type(user))

            # Llamar al servicio para crear el usuario
            result = service.create(user)
            return result  # El servicio ya maneja la redirección o los mensajes de error

        # Si es una petición GET, mostrar el formulario de creación
        return render_template('create_user.html')  # Tu plantilla HTML para crear usuarios

    except Exception as e:
        return jsonify({"error": str(e)}), 400