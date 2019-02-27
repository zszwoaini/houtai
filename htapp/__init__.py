from flask import Flask
# from htapp import settings
from htapp.settings import config
from htapp.ext import init_ext
from htapp.urls_apis import init_api
from htapp.views import init_blue

def create_app(env):
    app = Flask(__name__)

    app.config.from_object(settings.config.get(env))

    init_ext(app)
    init_api(app)

    init_blue(app)

    return app
