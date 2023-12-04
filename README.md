# Command-Line-Task-Manager
# To-Do Task Manager

## Overview

This command-line task manager application can be made executable and run from any location on your computer. Follow the instructions below to set it up.

## Steps

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
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

### 4. Move the .pickle File to the Home Directory
To make the .pickle file accessible from anywhere, move it to the user's home directory and rename it to .todo.pickle. This file is hidden as it starts with a dot.
```bash
mv .todo.pickle ~/
```

### 5. Run the Task Manager
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
