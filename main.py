import json

# Load tasks from file
def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

# Add a task
def add_task(tasks, task):
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)

# Mark a task as complete
def complete_task(tasks, task_number):
    tasks[task_number]['completed'] = True
    save_tasks(tasks)

# Main program
tasks = load_tasks()
while True:
    command = input("Enter command (add, complete, show, exit): ")
    if command == 'add':
        task = input("Enter task: ")
        add_task(tasks, task)
    elif command == 'complete':
        task_number = int(input("Enter task number to complete: "))
        complete_task(tasks, task_number)
    elif command == 'show':
        for idx, task in enumerate(tasks):
            status = "done" if task['completed'] else "pending"
            print(f"{idx}: {task['task']} [{status}]")
    elif command == 'exit':
        break
