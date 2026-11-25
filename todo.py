import json
from pathlib import Path

DATA_FILE = Path("tasks.json")

def load_tasks():
    """Read tasks from the JSON file. Return an empty list if none exist yet."""

    if not DATA_FILE.exists():
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Warning: tasks.json was corrupted. Starting fresh.")
        return []

def save_tasks(tasks):
    """Write tasks to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    """Print all tasks with numbers and a done/not-done mark."""
    if not tasks:
        print("\nNo tasks yet. Add one!")
        return
    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        mark = "[x]" if task["done"] else "[]"
        print(f" {number}. {mark} {task['title']}")

def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task can't be empty.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: {title}")

def get_task_number(tasks, action):
    """Ask for a valid task number and return its index, or None."""
    show_tasks(tasks)
    if not tasks:
        return None

    try:
        number = int(input(f"Number of task to {action}: "))
    except ValueError:
        print("Please type a valid number.")
        return None

    if 1 <= number <= len(tasks):
        return number - 1
    print("That number isn't in the list.")
    return None

def complete_task(tasks):
    """Mark a task as done."""
    index = get_task_number(tasks, "complete")
    if index is not None:
        tasks[index]["done"] = True
        save_tasks(tasks)
        print(f"Completed: {tasks[index]['title']}")

def delete_task(tasks):
    """Delete a task."""
    index = get_task_number(tasks, "delete")
    if index is not None:
        removed= tasks.pop(index)
        save_tasks(tasks)
        print(f"Deleted: {removed['title']}")

def main():
    tasks = load_tasks()
    menu = (
        "\n=== To-Do List ===\n"
        "1. Show tasks\n"
        "2. Add task\n"
        "3. Complete task\n"
        "4. Delete task\n"
        "5. Quit\n"
    )

    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()            