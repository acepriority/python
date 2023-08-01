import tkinter as tk
import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero."
    
def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def log(x):
    return math.log10(x)

def tan(x):
    return math.tan(math.radians(x))



def calculate():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operation = operations.get()

    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)
    elif operation == "Logarithm":
        result = log(num1)
    elif operation == "Sine":
        result = sine(num1)
    elif operation == "Cosine":
        result = cosine(num1)
    elif operation == "Tangent":
        result = tan(num1)

    result_label.config(text="Result: " + str(result))

# Create the main application window
root = tk.Tk()
root.title("Scientific Calculator")

# Input fields for numbers
entry_num1 = tk.Entry(root, width=10)
entry_num1.pack(pady=5)

entry_num2 = tk.Entry(root, width=10)
entry_num2.pack(pady=5)

# Dropdown menu for operations
operations = tk.StringVar()
operations.set("Add")
operation_choices = ["Add", "Subtract", "Multiply", "Divide", "Logarithm", "Sine", "Cosine", "Tangent"]
operation_menu = tk.OptionMenu(root, operations, *operation_choices)
operation_menu.pack(pady=5)

# Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

root.mainloop()
