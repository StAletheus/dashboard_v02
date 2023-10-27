from flask import Blueprint, render_template
from ..utils.openai_api import get_models

bp = Blueprint('dalle', __name__, url_prefix='/dalle')

@bp.route('/')
def index():
    models = get_models()
    return render_template('dalle.html', models=models)