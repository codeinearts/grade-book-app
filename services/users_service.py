from repositories.repository import Repository
from flask import render_template


class Service:
    def __init__(self):
        self.repository = Repository()

    def create(self) -> str:
        return render_template('in-construction.html')

    def read(self) -> str:
        return render_template('in-construction.html')
