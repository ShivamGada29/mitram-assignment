from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql+pymysql://root:@localhost:3306/mitram", echo=False)

SessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

Base = declarative_base()


#Dependency
def get_db():
    db = SessionLocal()
    try : 
        yield db
    finally:
        db.close()