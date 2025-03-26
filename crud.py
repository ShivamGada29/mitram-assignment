from sqlalchemy.orm import Session

from models.tasks import Task
from schema.serializer import TaskCreate, TaskUpdate, TaskId


def create_task(db: Session, task: TaskCreate):
    """Creates a Task"""
    try:
        db_task = Task(title=task.title, status=task.status)

        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception as e:
        db.rollback()
        print(e)
    return db_task


def get_all_tasks(db: Session):
    """View all Tasks"""
    return db.query(Task).all()


def update_task(db: Session, task_update: TaskUpdate):
    """Update a task based on Id"""
    db_task = db.query(Task).filter(Task.id == str(task_update.id)).first()
    
    if not db_task:
        return None
    
    if db_task.title is not None:
        db_task.title = task_update.title

    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: TaskId):
    """Delete a task based on Id"""
    db_task = db.query(Task).filter(Task.id == str(task_id.id)).first()
    
    if not db_task:
        return None

    db.delete(db_task)
    db.commit()
    return {'task':'deleted'}