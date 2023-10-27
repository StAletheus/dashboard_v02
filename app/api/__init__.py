# app/api/__init__.py

from flask import Blueprint

bp = Blueprint('api', __name__)

from . import gpt_api, dalle_api
