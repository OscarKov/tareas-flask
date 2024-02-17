from Data.MemoryRepository import MemoryRepository


class TaskController:
    @staticmethod
    def add_task(name, description):
        repo = MemoryRepository()
        task = repo.add_task(name, description)
        return task

    @staticmethod
    def get_all_tasks():
        repo = MemoryRepository()
        return repo.all_tasks()

    @staticmethod
    def get_task_by_id(id):
        repo = MemoryRepository()
        return repo.get_by_id(id)

    @staticmethod
    def update_task(id, name, description):
        repo = MemoryRepository()
        return repo.update_task(id, name, description)

    @staticmethod
    def delete_task(id):
        repo = MemoryRepository()
        return repo.delete_task(id)
