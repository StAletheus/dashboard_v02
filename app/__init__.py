from flask import Flask

def create_app():
    app = Flask(__name__)

    # Here you can initialize your controllers and attach them as blueprints
    # For example:
    # from .controllers import gpt_controller, dalle_controller
    # app.register_blueprint(gpt_controller.bp)
    # app.register_blueprint(dalle_controller.bp)

    return app 