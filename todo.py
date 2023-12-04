#!/usr/bin/env python3
"""todo.py: Command line task manager application using object-oriented design."""

__author__ = "Abhyas Mall"
__email__ = "abhyas@uchicago.edu"

from datetime import datetime, date
import argparse
import pickle

class Task:
    """Representation of a task

    Attributes:
    - created - date
    - completed - date
    - name - string
    - unique id - number
    - priority - int value of 1, 2, or 3; 1 is default
    - due date - date, this is optional
    """
    max_task_id = 0  # Add a class variable to keep track of the maximum task ID
    def __init__(self, name, priority=1, due_date=None, unique_id=None, created=None, completed=None):
        # Initialize a task with various attributes
        if unique_id is None:
            Task.max_task_id += 1
            self.unique_id = Task.max_task_id
        else:
            self.unique_id = unique_id
            Task.max_task_id = max(Task.max_task_id, unique_id)
        self.name = name
        if priority is None:
            self.priority = 1
        else:
            self.priority = priority
        if created is None:
            current_date = datetime.now()
            self.created = current_date.replace(microsecond=0)
        else:
            self.created = created
        self.completed = completed
        self.due_date = due_date


    def __str__(self):
        # String representation of the task
        return f"Name:{self.name}, ID:{self.unique_id}, Created:{self.created}, Completed:{self.completed}, Due_Date:{self.due_date}, Priority: {self.priority}"

    def time_from_due_date(self):
        # Calculate and return time remaining from the due date
        if self.due_date:
            current_date = datetime.now().date()
            if self.due_date < current_date:
                days_remaining = (current_date - self.due_date).days
                return f"The due date has already passed by {days_remaining} days."
            elif self.due_date == current_date:
                return "The due date is today."
            else:
                days_remaining = (self.due_date - current_date).days
                return f"The due date is in {days_remaining} days."
        else:
            return None

class Tasks:
    def __init__(self):
        """Read pickled tasks file into a list"""
        # Initialize the Tasks object by loading tasks from a pickle file
        try:
            with open('.todo.pickle', 'rb') as file:
                saved_tasks = pickle.load(file)
                self.tasks = [Task(
                    name=task['name'],
                    priority=task['priority'],
                    due_date=task['due_date'],
                    unique_id=task['unique_id'],
                    created=task['created'],
                    completed=task['completed']
                ) for task in saved_tasks]
                if self.tasks:
                    Task.max_task_id = max(task.unique_id for task in self.tasks)
                else:
                    Task.max_task_id = 0
        except FileNotFoundError:
            self.tasks = []
            Task.max_task_id = 0

    def pickle_tasks(self):
        """Pickles your task list to a file"""
        # Save the tasks to a pickle file
        with open('.todo.pickle', 'wb') as file:
            # Create a list of dictionaries containing task attributes
            tasks_data = [
                {
                    'unique_id': task.unique_id,
                    'name': task.name,
                    'priority': task.priority,
                    'due_date': task.due_date,
                    'created': task.created,
                    'completed': task.completed
                }
                for task in self.tasks
            ]
            pickle.dump(tasks_data, file)

    def list_tasks(self):
        """List all tasks that have not been completed."""
        # Retrieve and display tasks that are not completed
        tasks_to_list = [task for task in self.tasks if task.completed is None]
        if not tasks_to_list:
            print("No tasks to list.")
            return
        print("Tasks to list:")
        tasks_to_list.sort(key=lambda x: (x.due_date if x.due_date else date.min, x.priority, x.created), reverse=True)
        self.display_tasks(tasks_to_list, list_view=True)

    def report_tasks(self):
        """List all tasks, including both completed and incomplete tasks."""
        # Display all tasks
        if not self.tasks:
            print("No tasks to report.")
            return

        max_task_name_length = max(len(task.name) for task in self.tasks)
        max_created_length = max(len(task.created.strftime("%a %b %d %H:%M:%S %Z %Y")) for task in self.tasks)
        max_completed_length = max(len(task.completed.strftime("%a %b %d %H:%M:%S %Z %Y")) if task.completed else 0 for task in self.tasks)

        self.display_tasks(self.tasks)

    def display_tasks(self, tasks_to_display, list_view=False):
        """Display tasks in a tabular format."""
        max_task_name_length = max(len(task.name) for task in tasks_to_display)
        max_created_length = max(len(task.created.strftime("%a %b %d %H:%M:%S %Z %Y")) for task in tasks_to_display)
        max_completed_length = max(len(task.completed.strftime("%a %b %d %H:%M:%S %Z %Y")) if task.completed else 0 for task in tasks_to_display)
        if list_view:
            print("ID   Age  Due Date   Priority   Task")
            print("--   ---  --------   --------   ----")
            for task in tasks_to_display:
                age = (datetime.now() - task.created).days
                due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else '-'
                print(f"{task.unique_id:<4} {age:<4} {due_date:<11} {task.priority:<9} {task.name}")
        else:
            print("ID   Age  Due Date   Priority   Task" + " " * (max_task_name_length - len("Task")) +
                  "  Created" + " " * (max_created_length - len("Created")) +
                  "   Completed" + " " * (max_completed_length - len("Completed")))
            print("--   ---  --------   --------   ----" + " " * (max_task_name_length - len("Task")) +
                  "  -------" + " " * (max_created_length - len("Created")) +
                  "   -------------------------" + " " * (max_completed_length - len("Completed")))
            for task in tasks_to_display:
                age = (datetime.now() - task.created).days
                due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else '-'
                created = task.created.strftime("%a %b %d %H:%M:%S %Z %Y")
                completed = task.completed.strftime("%a %b %d %H:%M:%S %Z %Y") if task.completed else '-'
                print(f"{task.unique_id:<4} {age:<4} {due_date:<11} {task.priority:<9} {task.name:<{max_task_name_length}} "
                      f"{created:<{max_created_length}} {completed:<{max_completed_length}}")

    def add_task(self, task_name, priority=None, due_date=None):
        """Add a new task to the task list."""
        # Add a new task to the list
        if priority is None:
            priority = get_priority_input()
        if due_date is None:
            due_date = get_due_date_input()
        max_task_id = max((task.unique_id for task in self.tasks), default=0)
        task = Task(task_name, priority, due_date, unique_id=max_task_id + 1)
        self.tasks.append(task)
        print(f"Created task {task.unique_id}")
        self.pickle_tasks()

    def delete_task(self, task_id):
        """Delete a task from the task list."""
        # Delete a task by ID
        for task in self.tasks:
            if task.unique_id == task_id:
                self.tasks.remove(task)
                print(f"Deleted task {task_id}")
                self.pickle_tasks()
                return
        print(f"No task with ID {task_id} found.")

    def done_task(self, task_id):
        """Mark a task as completed."""
        # Mark a task as completed by ID
        for task in self.tasks:
            if task.unique_id == task_id:
                if task.completed is None:
                    task.completed = datetime.now().replace(microsecond=0)
                    # Update the task in the list
                    self.pickle_tasks()
                else:
                    print(f"Task {task_id} is already completed.")
                return
        print(f"No task with ID {task_id} found.")

    def query_tasks(self, query_terms):
        """Search for incompleted tasks that match search terms."""
        # Search for tasks that match query terms
        tasks_to_query = [task for task in self.tasks if task.completed is None]
        for term in query_terms:
            tasks_to_query = [task for task in tasks_to_query if term.lower() in task.name.lower()]
        if not tasks_to_query:
            print("No matching tasks found.")
            return
        tasks_to_query.sort(key=lambda x: (x.due_date if x.due_date else datetime.min, x.priority), reverse=True)
        self.display_tasks(tasks_to_query, list_view=True)

def get_priority_input():
    """Get priority input from user."""
    # Get priority input from the user
    while True:
        try:
            priority = int(input("Enter the priority (1, 2, or 3), or press Enter to use default (1): ") or 1)
            if priority not in [1, 2, 3]:
                raise ValueError('Priority must be 1, 2, or 3')
        except ValueError as ve:
            print(ve)
        else:
            break
    return priority

def get_due_date_input():
    """Get due date input from user."""
    # Get due date input from the user
    while True:
        try:
            due_date_input = input("Enter the due date (YYYY-MM-DD), or press Enter to skip: ")
            if not due_date_input:
                due_date_date = None  # Set due_date to None if the user skips
            else:
                due_date = datetime.strptime(due_date_input, "%Y-%m-%d")
                current_date = datetime.now().date()
                due_date_date = due_date.date()
                if due_date_date < current_date:
                    raise Exception('The due date must be greater or equal to today\'s date')
        except ValueError:
            print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        except Exception as e:
            print(e)
        else:
            break
    return due_date_date

def main():
    """Main function to handle command-line arguments."""
    # Main function to handle command-line arguments
    print('Welcome to: To do - Task Manager')
    parser = argparse.ArgumentParser(description='To do - Task Manager')
    parser.add_argument('--add', type=str, required=False, help='A task string that needs to be added to your list.')
    parser.add_argument('--list', action='store_true', required=False, help='list all tasks that have not been completed.')
    parser.add_argument('--delete', type=int, required=False, help='Delete a task by ID.')
    parser.add_argument('--done', type=int, required=False, help='Complete a task by ID.')
    parser.add_argument('--report', action='store_true', required=False, help='List all tasks, including completed tasks.')
    parser.add_argument('--query', type=str, required=False, nargs="+", help='Add query keywords; eg --query milk egg.')
    parser.add_argument('--priority', type=int, required=False, help='Priority for the task.')
    parser.add_argument('--due', type=str, required=False, help='Due date for the task in the format YYYY-MM-DD.')
    args, _ = parser.parse_known_args()  # Ignore unrecognized arguments
    task_manager = Tasks()
    if args.add:
        new_task_name = args.add
        # Validate priority
        priority = args.priority if args.priority is not None else None
        if priority is not None and priority not in [1, 2, 3]:
            print("Error: Priority must be 1, 2, or 3.")
            return
        # Validate due date
        due_date = args.due if args.due is not None else None
        if due_date is not None:
            try:
                due_date = datetime.strptime(due_date, "%Y-%m-%d").date()
                current_date = datetime.now().date()
                # Check if the due date is in the past
                if due_date < current_date:
                    print("Error: Due date must be today or a future date.")
                    return
            except ValueError:
                print("Error: Invalid date format. Please enter the date in the format YYYY-MM-DD.")
                return
        # Add the task
        task_manager.add_task(new_task_name, priority, due_date)
    elif args.list:
        task_manager.list_tasks()
    elif args.report:
        task_manager.report_tasks()
    elif args.query:
        task_manager.query_tasks(args.query)
    elif args.done:
        task_manager.done_task(args.done)
    elif args.delete:
        task_manager.delete_task(args.delete)
    else:
        parser.error("There was an error in creating your task. Run 'todo -h' for usage instructions.")

if __name__ == '__main__':
    main()