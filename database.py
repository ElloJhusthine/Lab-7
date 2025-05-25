 # database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = os.environ.get("postgresql://mypit3_user:G1Vcssc2qPp3uG6Kn3214qbrQBoK7DXI@dpg-cvpqe0k9c44c73duviq0-a.oregon-postgres.render.com/mypit3_db")
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

