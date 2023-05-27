from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

engine = create_engine(
    # "postgresql+psycopg2://repl:S3cretPassw0rd@localhost:5432/campdata_prod"
    "postgresql+psycopg2://admin:admin@localhost:5432/property_price"
)
session = Session(engine)
Base = declarative_base()
