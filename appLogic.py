from tkinter import *
from tkinter import messagebox

# List to store all the tasks submitted
task_list = []

# Counter to count the number of tasks
counter = 1

# Function to check for input error (blank text box when you hit submit)
def inputError():
    # If textbox is empty, show an error message and return 0 (indicating an input error)
    if enterTaskField.get() == "":
        messagebox.showerror("Input Error", "Task cannot be empty")
        return 0
    return 1

# Function to clear the number from the textbox where you enter the task number to delete
def clear_taskNumberField():
    # Delete all content from the taskNumberField
    taskNumberField.delete(0.0, END)

# Function to clear the task from the textbox where you enter the task to add
def clear_taskField():
    # Delete all content from the enterTaskField
    enterTaskField.delete(0, END)

# Function to insert a task into the task-area (numbered section)
def insertTask(event=None):
    global counter

    # Check for input error with the inserted value (task)
    value = inputError()
    if value == 0:
        return

    # Get the content from the enterTaskField
    content = enterTaskField.get() + "\n"
    # Add the task to the task_list
    task_list.append(content)

    # Insert the task into the task area within the GUI window
    TextArea.insert('end -1 chars', "[ " + str(counter) + " ] " + content)

    counter += 1
    clear_taskField()

# Function to delete a task
def delete():
    global counter

    # Check if there are no tasks
    if len(task_list) == 0:
        messagebox.showerror("No Task", "There are no tasks to delete")
        return

    # Get the task number to delete from the taskNumberField
    number = taskNumberField.get(1.0, END)

    # Check if the task number is empty
    if number == "\n":
        messagebox.showerror("Input Error", "Please enter a task number to delete")
        return

    try:
        # Convert the task number to an integer
        task_no = int(number)
    except ValueError:
        messagebox.showerror("Input error", "Invalid task number")
        return

    # Check if the task number is out of bounds
    if task_no < 1 or task_no > len(task_list):
        messagebox.showerror("Input error", "Task number out of bounds")
        return

    # Clear the taskNumberField
    clear_taskNumberField()

    # Remove the task from the task_list
    task_list.pop(task_no - 1)
    counter -= 1

    # Clear the entire TextArea
    TextArea.delete(1.0, END)

    # Insert the updated task list into the TextArea
    for i in range(len(task_list)):
        TextArea.insert('end -1 chars', "[ " + str(i + 1) + " ] " + task_list[i])

# Function to exit the application
def exit_app():
    gui.destroy()

# Code running the app
if __name__ == "__main__":
    # Creating the GUI window
    gui = Tk()
    gui.configure(bg="#CDB79E")
    gui.title("Task Management App")
    gui.geometry("290x310")

    # Creating GUI elements
    enterTask = Label(gui, text="Enter Your Task Below:", bg="#8B7D6B", font=("Arial", 18))
    enterTaskField = Entry(gui)
    Submit = Button(gui, text="Submit", fg="black", bg="white", command=insertTask)
    TextArea = Text(gui, height=5, width=28, font=("Arial", 15))
    taskNumber = Label(gui, text="Enter # of Task you'd like to delete:", bg="#8B7D6B", font=("Arial", 18))
    taskNumberField = Text(gui, height=1, width=2, font=("Arial", 15))
    delete_button = Button(gui, text="Delete", fg="black", bg="white", command=delete)
    Exit = Button(gui, text="Close App", fg="black", bg="white", command=exit_app)

    # Placing GUI elements within the window
    enterTask.grid(row=0, column=2)
    enterTaskField.grid(row=1, column=2, ipadx=40)
    Submit.grid(row=2, column=2)
    TextArea.grid(row=3, column=2, padx=15, sticky=W)
    taskNumber.grid(row=4, column=2, pady=5)
    taskNumberField.grid(row=5, column=2)
    delete_button.grid(row=6, column=2, pady=5)
    Exit.grid(row=7, column=2)

    # Binding the Enter key to the insertTask function
    gui.bind('<Return>', insertTask)

    # Starting the GUI
    gui.mainloop()
