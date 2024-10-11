# app.py
from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from controllers.users_controller import users_bp
from controllers.tasks_controller import tasks_bp

app = Flask(__name__)
# Habilitar el modo de depuración
app.config["DEBUG"] = True
# Disable strict slashes globally
app.url_map.strict_slashes = False
# Establecer el SECRET_KEY
# TODO: Cambia esto a una clave secreta única y segura
app.config['SECRET_KEY'] = "yuta&rika"

toolbar = DebugToolbarExtension(app)

app.register_blueprint(users_bp)
# app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(tasks_bp, url_prefix="/tasks")

@app.route("/", methods=["GET"])
def read():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
