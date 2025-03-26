from fastapi import FastAPI

from api.routes import router
from models import mysqldb

mysqldb.Base.metadata.create_all(bind=mysqldb.engine)
app = FastAPI()

def get_db():
    db = mysqldb.SessionLocal()
    try : 
        yield db
    finally:
        db.close()

app.include_router(router)