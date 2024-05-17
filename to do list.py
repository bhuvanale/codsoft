import tkinter as tk
import json

class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} [{status}]"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)

    def update_task(self, index, new_description):
        if 0 <= index < len(self.tasks):
            self.tasks[index].description = new_description

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def list_tasks(self):
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                tasks_data = json.load(f)
                self.tasks = [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            print(f"No such file: '{filename}'")

class ToDoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        self.todo_list = todo_list
        self.title("To-Do List")
        self.geometry("400x400")

        self.task_entry = tk.Entry(self)
        self.task_entry.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(self)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)

        self.update_button = tk.Button(self, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.complete_button = tk.Button(self, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.load_tasks()

    def add_task(self):
        description = self.task_entry.get()
        if description:
            self.todo_list.add_task(description)
            self.refresh_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_description = self.task_entry.get()
            self.todo_list.update_task(index, new_description)
            self.refresh_tasks()

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.complete_task(index)
            self.refresh_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.delete_task(index)
            self.refresh_tasks()

    def refresh_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list.tasks:
            self.task_listbox.insert(tk.END, task)
        self.task_entry.delete(0, tk.END)

    def load_tasks(self):
        self.todo_list.load_tasks("tasks.txt")
        self.refresh_tasks()

def print_menu():
    print("\nTo-Do List Application")
    print("1. Add Task")
    print("2. Update Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. List Tasks")
    print("6. Save Tasks")
    print("7. Load Tasks")
    print("8. GUI Mode")
    print("9. Exit")

def main():
    todo_list = ToDoList()
    filename = "tasks.txt"

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            new_description = input("Enter new description: ")
            todo_list.update_task(index, new_description)
        elif choice == '3':
            index = int(input("Enter task number to complete: ")) - 1
            todo_list.complete_task(index)
        elif choice == '4':
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == '5':
            todo_list.list_tasks()
        elif choice == '6':
            todo_list.save_tasks(filename)
            print("Tasks saved.")
        elif choice == '7':
            todo_list.load_tasks(filename)
            print("Tasks loaded.")
        elif choice == '8':
            app = ToDoApp(todo_list)
            app.mainloop()
        elif choice == '9':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
