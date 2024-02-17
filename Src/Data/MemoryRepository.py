from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select, update
from .Entities import Task


class MemoryRepository:

    def __init__(self):
        self.engine = create_engine("sqlite:///tasks.db", echo=True)

    def add_task(self, name, description):
        session = Session(self.engine)
        task = Task(name=name, description=description)
        session.add(task)
        session.commit()
        return task

    def all_tasks(self):
        session = Session(self.engine)
        stmt = select(Task)
        return session.scalars(stmt).all()

    def get_by_id(self, id):
        session = Session(self.engine)
        task = session.get(Task, id)
        return task

    def update_task(self, id, newName, newDescription):
        session = Session(self.engine)
        stmt = (
            update(Task)
            .where(Task.id == id)
            .values(name=newName, description=newDescription)
        )
        session.execute(stmt)
        session.commit()

        task = session.query(Task).filter(Task.id == id).one()
        return task

    def delete_task(self, id):
        session = Session(self.engine)
        task = session.get(Task, id)
        session.delete(task)
        session.commit()
        return task
