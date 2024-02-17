from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h2>Tasks App</h2>"

@app.route("/tasks/")
def tasks_list():
    return []

@app.route("/tasks/<int:task_id>", methods = ['GET', 'PATCH'])
def get_task():
    return {}

@app.route("/tasks/add", methods = ['POST'])
def add_task():
    return "<p>Hello, World!</p>"

@app.route("/task/update", methods = ['PUT', 'PATCH'])
def update_task():
    return "<p>Hello, World!</p>"

@app.route("/task/<int:task_id>", methods = ['DELETE'])
def delete_task():
    return "<p>Hello, World!</p>"