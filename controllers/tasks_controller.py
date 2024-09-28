from flask import request, redirect, url_for, Blueprint, render_template

from services.tasks_service import Service

tasks_bp = Blueprint("tasks", __name__)
service = Service()

in_construction = 'in-construction.html'

@tasks_bp.route('/tasks', methods=['GET'])
def read():
    return service.read()

@tasks_bp.route('/tasks/create', methods=['GET'])
def create():
    return service.create()

@tasks_bp.route('/tasks/update', methods=['GET'])
def update():
    return service.update()

@tasks_bp.route('/tasks/delete', methods=['GET'])
def delete():
    return service.delete()
