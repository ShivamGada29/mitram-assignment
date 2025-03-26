import httpx
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from schema.serializer import TaskCreate, TaskSerializer, TaskUpdate, TaskId
from models.mysqldb import get_db
from models.status import StatusEnum

from dotenv import load_dotenv
import logging
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(f'{BASE_DIR}/.env')

MITRAM_URL = os.getenv("MITRAM_URL")



logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
router = APIRouter()

@router.get('/')
async def home(db:Session=Depends(get_db)):
    db_task = crud.get_all_tasks(db=db)
    return db_task


@router.post('/', response_model=TaskSerializer)
async def create_task(task: TaskCreate, db:Session=Depends(get_db)):
    status = ''
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(MITRAM_URL)

            if response.status_code == 200:
                status = response.json().get("status")
                print(status)
            else:
                logger.error(f"Failed request: {response.status_code} - {response.text}")
    except (Exception) as e:
        logger.error(f"External API request failed: {str(e)}")

    if status:
        print('Hey', status)
        task.status = StatusEnum(status)

    db_task = crud.create_task(db=db, task=task)
    logger.info(f'LOGGER {db_task.__dict__}')
    return db_task


@router.put('/', response_model=TaskSerializer)
async def update_task(task_update:TaskUpdate, db:Session=Depends(get_db)):
    if not task_update.title:
        raise HTTPException(status_code=404, detail="Title not Found")
    task_update = crud.update_task(db=db, task_update=task_update)
    if not task_update:
        raise HTTPException(status_code=404, detail="Task not Found")
    return task_update


@router.delete('/', response_model=dict)
async def delete_task(task_id:TaskId, db:Session=Depends(get_db)):
    task_delete = crud.delete_task(task_id=task_id, db=db)
    if not task_delete:
        raise HTTPException(status_code=404, detail="Task not Found")
    return task_delete