to_do_list = []

def to_do_list_tasks():
    print("\n *** To_Do_List *** ")
    print("1. Track Tasks")
    print("2. Create Task")
    print("3. Update Task")
    
def track_tasks():
    if not to_do_list:
        print("Your to-do-list is empty.")
    else:
        for index, task in enumerate(to_do_list, start=1):
            status = "✓" if task['done'] else "✗"
            print(f"{index}. [{status}] {task['task_name']}")


def create_task():
    task_name = input("Enter the task: ")
    to_do_list.append({'task_name': task_name, 'done': False})
    print("task created.")

def update_task():
    track_tasks()
    try:
        task_num = int(input("Enter the task number to update: "))
        new_task_name = input("Enter the new task name: ")
        to_do_list[task_num - 1]['title'] = new_task_name
        print("Task updated.")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    to_do_list_tasks()
    choice = input("Enter your choice: ")

    if choice == '1':
        track_tasks()
    elif choice == '2':
        create_task()
    elif choice == '3':
        update_task()
        break
    else:
        print("Invalid choice. Please try again.")