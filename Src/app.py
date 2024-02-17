from flask import Flask, request, jsonify

from Controllers.TaskController import TaskController

app = Flask(__name__)


@app.route("/")
def index():
    return "<h2>Tasks App</h2>"


@app.route("/tasks/")
def task_list():
    task_list = TaskController.get_all_tasks()
    return task_list


@app.route("/tasks/<int:task_id>", methods=['GET', 'PATCH'])
def get_task(task_id):
    task = TaskController.get_task_by_id(task_id)
    return jsonify(task)


@app.route("/tasks/add", methods=['POST'])
def add_task():
    name = request.form['name']
    description = request.form['description']
    task = TaskController.add_task(name, description)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=['PUT', 'PATCH'])
def update_task(task_id):
    name = request.form['name']
    description = request.form['description']
    task = TaskController.update_task(task_id, name, description)
    return jsonify(task)


@app.route("/tasks/<int:task_id>", methods=['DELETE'])
def delete_task(task_id):
    task = TaskController.delete_task(task_id)
    return jsonify(task)
