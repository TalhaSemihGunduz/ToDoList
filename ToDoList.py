# Simple To-Do List Application

def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for i, (task, completed) in enumerate(tasks, 1):
            status = "✓" if completed else "✗"
            print(f"{i}. {task} [{status}]")

def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append((task, False))
    print(f"Task '{task}' added to the list.")

def mark_task_completed(tasks):
    if not tasks:
        print("No tasks to mark as completed.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks[task_num - 1]
            tasks[task_num - 1] = (task, True)
            print(f"Task '{task}' marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            task, _ = tasks.pop(task_num - 1)
            print(f"Task '{task}' deleted from the list.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()