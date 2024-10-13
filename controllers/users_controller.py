from flask import request, redirect, url_for, Blueprint, render_template, jsonify, flash
from services.users_service import Service
from utils.commons.users_data_models import User
# from wtforms import Form, StringField, validators  # Podrías usar WTForms para validaciones adicionales
import logging

# Configurar el logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

users_bp = Blueprint("users", __name__)
service = Service()


@users_bp.route("/users", methods=["GET"])
def read():
    """
    Lee y devuelve la lista de usuarios.
    """
    try:
        return service.read()
    except Exception as e:
        logger.error(f"Error leyendo usuarios: {e}")
        return jsonify({"error": "Error al obtener la lista de usuarios"}), 500


@users_bp.route("/echo", methods=["GET"])
def echo():
    """
    Devuelve el valor de echo pasado como parámetro de consulta.
    Ejemplo: http://127.0.0.1:5000/echo?echo=echo+this+back+to+me
    """
    try:
        to_echo = request.args.get("echo", "")
        response = "{}".format(to_echo)
        return response
    except Exception as e:
        logger.error(f"Error en echo: {e}")
        return jsonify({"error": "Error en la operación echo"}), 400


@users_bp.route("/user/create", methods=["GET", "POST"])
def create():
    """
    Crea un nuevo usuario a partir de los datos del formulario. 
    Si es una solicitud GET, se muestra el formulario de creación.
    Si es una solicitud POST, valida los datos y crea el usuario.
    """
    try:
        if request.method == 'POST':
            user_data = request.form.to_dict()

            # Validaciones adicionales (si es necesario)
            if not user_data.get("username"):
                return jsonify({"error": "El campo username es obligatorio"}), 400

            # Crear y validar el usuario
            user = User(**user_data)
            logger.info(f"Usuario validado: {user}")
            
            # Crear el usuario usando el servicio
            result = service.create(user)
            flash("Usuario creado con éxito", "success")

            # Redirigir después de la creación exitosa
            return redirect(url_for("users.read"))

        # En caso de GET, renderizar el formulario
        return render_template('create_user.html')

    except ValueError as ve:
        logger.warning(f"Error de validación: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logger.error(f"Error creando usuario: {e}")
        return jsonify({"error": "Error interno al crear el usuario"}), 500
