# Command-Line-Task-Manager
# To-Do Task Manager

## Overview

This Python-based command-line application is designed to help manage your tasks efficiently. It allows you to add, list, delete, and mark tasks as completed right from your terminal. The tasks are stored in a pickled file, ensuring that your data persists across sessions.

The application is built using object-oriented programming (OOP) principles, which makes the code modular, reusable, and easy to maintain. Here's a brief overview of the classes used:

1. **Task**: This class represents a single task. Each task has attributes such as `name`, `priority`, `due_date`, `unique_id`, `created`, and `completed`. The class also includes methods for string representation of the task and calculating the time remaining from the due date.

2. **Tasks**: This class represents a collection of tasks. It includes methods for pickling (saving) tasks to a file, listing all tasks, reporting tasks, displaying tasks in a tabular format, adding a new task, deleting a task, marking a task as completed, and querying tasks based on search terms.

The application uses the argparse module to handle command-line arguments, allowing users to interact with their task list directly from the terminal. This includes adding new tasks, listing all tasks, deleting tasks, marking tasks as completed, and querying tasks.

In summary, this application is an example of how OOP can be used to build a powerful tool. The code is well-structured and easy to understand, making it a good starting point for anyone interested in learning more about Python and OOP.

#### Note: This command-line task manager application can be made executable and run from any location on your computer. Follow the instructions below to set it up.
## Steps

### 1. Clone the Repository

```bash
git clone https://github.com/abhyas01/Command-Line-Task-Manager
cd Command-Line-Task-Manager
```

### 2. Change the Running Mode
```bash
chmod +x todo.py
```

### 3. Move the Script to a Directory in $PATH
Choose a directory that is included in your system's $PATH variable. Common choices include /usr/local/bin on Unix-like systems.
```bash
sudo mv todo.py /usr/local/bin/todo
```

### 4. Run the Task Manager
Now you can run the task manager from any location using the following command:
```bash
todo
```

# Usage
## Add a task
todo --add "Buy groceries" --priority 2 --due 2023-12-31

## List tasks
todo --list

## Mark a task as done
todo --done 1

## Delete a task
todo --delete 2

## Report all tasks
todo --report

## Query tasks
todo --query groceries

# Example:

```bash
todo --add "Buy Milk"
# Output:
# Enter the priority (1, 2, or 3), or press Enter to use default (1): 5
# Priority must be 1, 2, or 3
# Enter the priority (1, 2, or 3), or press Enter to use default (1): 2
# Enter the due date (YYYY-MM-DD), or press Enter to skip:
# Created task 3

todo --add "Buy Milk"
# Output:
# Enter the priority (1, 2, or 3), or press Enter to use default (1):
# Enter the due date (YYYY-MM-DD), or press Enter to skip: 2023-12-01
# The due date must be greater or equal to today's date
# Enter the due date (YYYY-MM-DD), or press Enter to skip:
# Created task 4

todo --add "Buy Milk" --priority 3
# Output:
# Enter the due date (YYYY-MM-DD), or press Enter to skip:
# Created task 5

todo --add "Buy Milk" --due 2023-12-10
# Output:
# Enter the priority (1, 2, or 3), or press Enter to use default (1):
# Created task 6
```

# Example in action

![example](https://github.com/abhyas01/Command-Line-Task-Manager/assets/91689587/ecc566c7-ef37-4450-8b4b-841cf8843c2b)

