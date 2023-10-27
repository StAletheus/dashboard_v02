from flask import Blueprint, render_template
import os
import openai


def get_models():
    response = openai.Model.list()
    return response['data']


api_key = os.environ.get('OPENAI_API_KEY')

if api_key is None:
    raise ValueError("API key must be set as an environment variable.")
# In controllers/gpt_controller.py


bp = Blueprint('gpt', __name__, url_prefix='/gpt')


@bp.route('/')
def index():
    models = get_models()
    return render_template('gpt.html', models=models)
