import os
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from controllers.users_controller import users_bp
from controllers.tasks_controller import tasks_bp

app = Flask(__name__)

# Configuración basada en entorno
# Usa variables de entorno para definir el modo de depuración y la clave secreta
app.config["DEBUG"] = os.environ.get("FLASK_DEBUG", "False").lower() in ["true", "1"]
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or os.urandom(24)

# Disable strict slashes globally
app.url_map.strict_slashes = False

# Configurar la barra de herramientas de depuración solo si está en modo DEBUG
if app.config["DEBUG"]:
    toolbar = DebugToolbarExtension(app)

# Registro de Blueprints
app.register_blueprint(users_bp)
app.register_blueprint(tasks_bp, url_prefix="/tasks")

# Ruta principal
@app.route("/", methods=["GET"])
def home():
    """Renderiza la página de inicio."""
    return render_template("home.html")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # El modo de depuración será determinado por la configuración de entorno
    app.run(debug=app.config["DEBUG"])
