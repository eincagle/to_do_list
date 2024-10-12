# To-Do List Command-Line Application

## Overview
The **To-Do List Command-Line Application** is a simple and efficient tool for managing tasks directly from the command line. Users can add tasks, mark them as complete, and view the status of all tasks. The tasks are stored in a JSON file to persist across sessions.

## Features
- **Add Tasks**: Easily add tasks that are saved and available across sessions.
- **Complete Tasks**: Mark tasks as complete once they are done.
- **View All Tasks**: Display all tasks along with their status (`pending` or `done`).
- **Persistent Storage**: Tasks are saved in a `JSON` file to ensure they are not lost between uses.

## Technologies Used
- **Python**: Core programming language.
- **JSON**: Used to store tasks across sessions.

## How to Run the Project

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/to-do-list-cli.git
    cd to-do-list-cli
    ```

2. **Run the Application**:
    ```bash
    python todo.py
    ```

3. **Available Commands**:
   - **Add a Task**:  
     Type `add` to add a new task to your to-do list.  
     Example:
     ```bash
     Enter command (add, complete, show, exit): add
     Enter task: Finish the Python project
     ```

   - **Complete a Task**:  
     Type `complete` to mark a task as complete.  
     Example:
     ```bash
     Enter command (add, complete, show, exit): complete
     Enter task number to complete: 0
     Task completed!
     ```

   - **Show All Tasks**:  
     Type `show` to display all tasks and their status (`pending`/`done`).  
     Example:
     ```bash
     Enter command (add, complete, show, exit): show
     0: Finish the Python project [pending]
     ```

   - **Exit the Program**:  
     Type `exit` to close the program.

## Example Usage
```bash
# Adding a task
Enter command (add, complete, show, exit): add
Enter task: Finish Python project

# Showing all tasks
Enter command (add, complete, show, exit): show
0: Finish Python project [pending]

# Completing a task
Enter command (add, complete, show, exit): complete
Enter task number to complete: 0
Task completed!

# Showing tasks again
Enter command (add, complete, show, exit): show
0: Finish Python project [done]

# Exit the program
Enter command (add, complete, show, exit): exit
