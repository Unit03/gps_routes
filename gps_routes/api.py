import connexion

from . import db, settings


connexion_app = connexion.App(__name__)
connexion_app.add_api(settings.SWAGGER_FILE_PATH, validate_responses=True)
app = connexion_app.app

db.initialize(settings.SQL_DSN)
