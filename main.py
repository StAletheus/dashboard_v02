from flask import Flask
from config import Config
from .controllers import gpt_controller, dalle_controller
app.register_blueprint(gpt_controller.bp)
app.register_blueprint(dalle_controller.bp)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Register the blueprints
    app.register_blueprint(gpt_controller.bp)
    app.register_blueprint(dalle_controller.bp)

    return app

app = create_app()

if __name__ == "__main__":
    app.run()