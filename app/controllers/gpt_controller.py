from flask import Blueprint, render_template
from ..utils.openai_api import get_models

bp = Blueprint('gpt', __name__, url_prefix='/gpt')


@bp.route('/')
def index():
    models = get_models()
    return render_template('gpt.html', models=models)
