# tasks.py
import json

def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task, filename="tasks.json"):
    tasks = load_tasks(filename)
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks, filename)

def complete_task(index, filename="tasks.json"):
    tasks = load_tasks(filename)
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        save_tasks(tasks, filename)

def list_tasks(filename="tasks.json"):
    tasks = load_tasks(filename)
    return tasks
