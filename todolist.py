def show_menu():
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Exit")
    return input("Enter your choice: ")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    else:
        print("No tasks.")

def mark_task_done(tasks):
    view_tasks(tasks)
    if tasks:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task marked as done.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        choice = show_menu()
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
main()
