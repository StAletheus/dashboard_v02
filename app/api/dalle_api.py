# app/api/dalle_api.py

from flask import jsonify
from . import bp

@bp.route('/get_dalle_models', methods=['GET'])
def get_dalle_models():
    models = ['dalle-1.0', 'dalle-mini']
    return jsonify(models)
