# app/api/gpt_api.py

from flask import jsonify
from . import bp

@bp.route('/get_models', methods=['GET'])
def get_models():
    models = ['gpt-3.5-turbo', 'text-davinci-002']
    return jsonify(models)
