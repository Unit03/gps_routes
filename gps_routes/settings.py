import os
import pathlib


SWAGGER_FILE_PATH = pathlib.Path(__file__).parent / "swagger.yml"

SQL_DSN = os.environ.get(
    "SQL_DSN", "postgresql+psycopg2://postgres@127.0.0.1/5432",
)
