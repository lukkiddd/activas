from flask import Flask
from .apis import blueprint


app = Flask(__name__)
app.register_blueprint(blueprint)
