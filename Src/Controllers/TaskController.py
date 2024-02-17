from Data import MemoryRepository 

class TaskController:

    def add_task(name, description):
        repo = MemoryRepository()
        task = repo.add_task(name, description)
        return task

    def get_all_tasks():  
        repo = MemoryRepository()
        return repo.all_tasks()

    def get_task_by_id(id):
        repo = MemoryRepository()
        return repo.get_by_id(id)

    def update_task(id, name, description):
        repo = MemoryRepository()
        return repo.update_task(id,name,description)

    def delete_task(id):
        repo = MemoryRepository()
        return repo.delete_task(id)
