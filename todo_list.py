import tkinter as tk
import json
from tkinter import messagebox

tasks = []

root = tk.Tk()
root.title("TO-DO List")
root.geometry("500x600")
root.configure(bg="light blue")

def add_task():
    task = entry.get().strip()

    if task != "":
        tasks.append(task)
        listbox.insert(tk.END , task)
        entry.delete(0 , tk.END)
        update_count()

def delete_task():  
    selected = listbox.curselection()

    if selected:
        number = selected[0]
        listbox.delete(number)
        tasks.pop(number)
        update_count()

def update_task():
    selected = listbox.curselection()
    new_task = entry.get().strip()

    if selected and new_task != "":
        number = selected[0]
        tasks[number] = new_task
        listbox.delete(number)
        listbox.insert(number , new_task)
        entry.delete(0 , tk.END)
        update_count()

def complete_task():
    selected = listbox.curselection()

    if selected:
        number = selected[0]
        task = listbox.get(number)

        if task.startswith("✓ "):
            task = task[2:]
        else:
            task = "✓ " + task

        tasks[number] = task
        listbox.delete(number)
        listbox.insert(number , task)

        listbox.selection_set(number)

        update_count()

def clear_tasks():
    tasks.clear()
    listbox.delete(0 , tk.END)

    with open ("tasks.json" , "w") as file:
        json.dump(tasks , file)
    update_count()

def save_tasks():
    if tasks:
        with open ("tasks.json" , "w") as file:
            json.dump(tasks , file)
        messagebox.showinfo("Saved" , "Task saved successfully!")

    else:
        messagebox.showwarning("Warning" , "There are no such tasks to save")

def load_tasks():
    try:
        with open("tasks.json" , "r") as file:
            saved_tasks = json.load(file)

        for task in saved_tasks:
            tasks.append(task)
            listbox.insert(tk.END , task)

    except FileNotFoundError:
        pass


def update_count():
    total = len(tasks)
    completed = 0

    for task in tasks:
        if task.startswith("✓ "):
            completed += 1

    count_label.config(
        text = "Total Tasks: " +str(total) +
        " | Completed:" + str(completed)            
        )


label = tk.Label(root , text = "My TO-DO List" , font = ("Arial", 24 , "bold") , bg = "light blue")
label.pack(pady=10)

entry = tk.Entry(root, width = 35 , font = ("Arial" , 14))
entry.pack(pady=10)

tk.Button(
    root,
    text = "Add Task",
    width = 15,
    font = ("Arial" , 11),
    command = add_task
).pack()

tk.Button(
    root,
    text = "Delete Task",
    width = 15,
    font = ("Arial" , 11),
    command = delete_task
).pack(pady=5)

tk.Button(
    root,
    text = "Update Task",
    width = 15,
    font = ("Arial" , 11),
    command = update_task
).pack(pady = 5)

tk.Button(
    root,
    text = "Complete Task",
    width = 15,
    font = ("Arial" , 11),
    command = complete_task
).pack(pady = 5)

tk.Button(
    root,
    text = "Clear ALL",
    width = 15,
    font = ("Arial" , 11),
    command = clear_tasks
).pack(pady = 5)

tk.Button(
    root,
    text = "Save Tasks",
    width = 15,
    font = ("Arial" , 11),
    command = save_tasks
).pack(pady=5)

listbox = tk.Listbox(root , width = 35 , height = 10 , font = ("Arial" , 13))
listbox.pack(pady=10)

count_label = tk.Label(
    root,
    text = "Total Tasks: 0 | Completed: 0",
    font = ("Arial" , 11),
    bg = "light blue"
    )
count_label.pack(pady=10)

load_tasks()
update_count()
root.mainloop()
