from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:Test123@localhost:32773/LOSTANDFOUND', echo=True)
Session = sessionmaker(bind=engine)

Base = declarative_base()
