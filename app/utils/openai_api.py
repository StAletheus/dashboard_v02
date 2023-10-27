import openai

openai.api_key = '.....'  # replace with your actual API key

def get_models():
    response = openai.Model.list()
    models = response['models']
    return models
```

And the controller should import from this location:

```python
# In controllers/gpt_controller.py

from flask import Blueprint, render_template
from ..utils.openai_api import get_models

bp = Blueprint('gpt', __name__, url_prefix='/gpt')

@bp.route('/')
def index():
    models = get_models()
    return render_template('gpt.html', models=models)
