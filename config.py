class Config:
    SECRET_KEY = "mysecretkey123"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:bazzinga@localhost:5432/leettrack"
    SQLALCHEMY_TRACK_MODIFICATIONS = False