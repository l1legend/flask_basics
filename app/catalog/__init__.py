# app/catalog/__init__.py

from flask import Blueprint
main = Blueprint('main', __name__, template_folder='template')

from app.catalog import routes

