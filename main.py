from flask import Flask
from flask import Flask, render_template
from config import Config
from app.api import bp as api_bp
from app.controllers import gpt_controller, dalle_controller

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def root_index():
        return render_template('index.html')

    # Register the blueprints
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(gpt_controller.bp)
    app.register_blueprint(dalle_controller.bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()