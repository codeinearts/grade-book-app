from flask import request, redirect, url_for, Blueprint, render_template

from services.service import Service

tasks_bp = Blueprint("tasks", __name__)
service = Service()

in_construction = 'in-construction.html'

@tasks_bp.route('/tasks', methods=['GET'])
def read():
    return render_template(in_construction)

@tasks_bp.route('/tasks/create', methods=['GET'])
def create():
    return render_template(in_construction)

@tasks_bp.route('/tasks/update', methods=['GET'])
def update():
    return render_template(in_construction)

@tasks_bp.route('/tasks/delete', methods=['GET'])
def delete():
    return render_template(in_construction)
