from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    # Register db handle
    from utils import init_app
    init_app(app)

    # Register blueprints
    from blueprints import root, questions
    app.register_blueprint(root.root_bp)
    app.register_blueprint(questions.questions_bp, url_prefix="/questions")
    return app
