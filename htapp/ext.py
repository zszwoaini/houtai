from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_caching import Cache
db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
cache = Cache()
# api = Api()


def init_ext(app):

    db.init_app(app)
    migrate.init_app(app,db=db)
    mail.init_app(app)
    cache.init_app(app,{'CACHE_TYPE':'redis'})

