from flask import Flask, request, jsonify

from Controllers.TaskController import TaskController

app = Flask(__name__)

taskController = TaskController()

@app.route("/")
def index():
    return "<h2>Tasks App</h2>"


@app.route("/tasks/")
def task_list():
    task_list = taskController.get_all_tasks()
    return task_list


@app.route("/tasks/<int:task_id>", methods=['GET', 'PATCH'])
def get_task(task_id):
    task = taskController.get_task_by_id(task_id)
    return jsonify(task)


@app.route("/tasks/add", methods=['POST'])
def add_task():
    name = request.form['name']
    description = request.form['description']
    task = taskController.add_task(name, description)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=['PUT', 'PATCH'])
def update_task(task_id):
    name = request.form['name']
    description = request.form['description']
    task = taskController.update_task(task_id, name, description)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    task = taskController.delete_task(task_id)
    return jsonify(task)
