import os


class Config:

    SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey123")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        "postgresql://postgres:bazzinga@localhost:5432/leettrack"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False