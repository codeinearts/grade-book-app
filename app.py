# app.py
from flask import Flask, render_template
from controllers.users_controller import users_bp
from controllers.tasks_controller import tasks_bp

app = Flask(__name__)

# Disable strict slashes globally
app.url_map.strict_slashes = False

app.register_blueprint(users_bp)
app.register_blueprint(tasks_bp)

@app.route('/', methods=['GET'])
def read():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
