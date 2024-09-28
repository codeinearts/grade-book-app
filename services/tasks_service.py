from repositories.tasks_repository import Repository
from flask import render_template

in_construction: str = "in-construction.html"

class Service:
    def __init__(self):
        self.repository = Repository()

    def create(self) -> str:
        return render_template(in_construction)

    def read(self) -> str:
        return render_template(in_construction)

    def update(self) -> str:
        return render_template(in_construction)

    def delete(self) -> str:
        return render_template(in_construction)

