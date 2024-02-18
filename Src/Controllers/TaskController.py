from Data.MemoryRepository import MemoryRepository


class TaskController:

    def __init__(self) -> None:
        self.repo = MemoryRepository()

    def add_task(self, name, description):
        task = self.repo.add_task(name, description)
        return task

    def get_all_tasks(self):
        return self.repo.all_tasks()

    def get_task_by_id(self, id):
        return self.repo.get_by_id(id)

    def update_task(self, id, name, description):
        return self.repo.update_task(id, name, description)

    def delete_task(self, id):
        return self.repo.delete_task(id)
