import tkinter as tk
from tkinter import messagebox
import math

def calculate_percentage(expression):
    """Calculate percentage in the expression."""
    operators = ['+', '-', '*', '/']
    for operator in operators:
        if operator in expression:
            # Split the expression based on the operator
            parts = expression.rsplit(operator, 1)
            if len(parts) == 2 and '%' in parts[1]:
                base_value = float(parts[0].strip())
                percentage_value = float(parts[1].replace('%', '').strip())
                
                # Calculate the percentage and apply it to the base value
                if operator == '+':
                    return str(base_value + (base_value * percentage_value / 100))
                elif operator == '-':
                    return str(base_value - (base_value * percentage_value / 100))
                elif operator == '*':
                    return str(base_value * (percentage_value / 100))
                elif operator == '/':
                    return str(base_value / (percentage_value / 100))
    
    return expression


def on_button_click(ch):
    try:
        if ch == 'C':
            input_field.delete(0, tk.END)
        elif ch == '⌫':
            input_field.delete(len(input_field.get()) - 1)
        elif ch == '=':
            expression = input_field.get()
            # Handle percentage calculation correctly
            if '%' in expression:
                expression = calculate_percentage(expression)
            input_field.delete(0, tk.END)
            input_field.insert(tk.END, str(eval(expression)))
        else:
            if ch in operations:
                num = float(input_field.get())
                result = operations[ch](math.radians(num) if ch in ['sin', 'cos', 'tan'] else num)
                input_field.delete(0, tk.END)
                input_field.insert(tk.END, str(result))
            elif ch == '.' and '.' not in input_field.get():
                input_field.insert(tk.END, ch)
            else:
                input_field.insert(tk.END, ch)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")

# Operations dictionary
operations = {
    '√': math.sqrt,
    'x²': lambda x: x**2,
    'x³': lambda x: x**3,
    'e^x': math.exp,
    'sin': math.sin,
    'cos': math.cos,
    'tan': math.tan,
}

# Create main window
root = tk.Tk()
root.title("Calculator: Debasis Baidya")
root.configure(bg='black')  # Set a black background color

# Input field with increased height
input_field = tk.Entry(root, font=('Arial', 24), justify='right', bg='lightgray', width=15)
input_field.grid(row=0, column=0, columnspan=4, pady=20, padx=20, sticky="nsew")

# Button layout
buttons = [
    ['√', 'x²', 'x³', '⌫'],
    ['sin', 'cos', 'tan', 'C'],
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '%', '+'],
    ['(', ')', '±', '=']
]

# Create buttons with adjusted size
def create_square_button(text, row, col):
    button = tk.Button(root, text=text, font=('Arial', 16), bg=colors.get(text, 'white'), fg='black', height=1, width=4,
                       command=lambda: on_button_click(text), relief='raised')
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    button['borderwidth'] = 0
    button['highlightthickness'] = 0

# Button colors
colors = {'+': 'lightblue', '-': 'lightblue', '*': 'lightblue', '/': 'lightblue', '=': 'lightgreen', 'C': 'red', '⌫': 'orange'}

# Create buttons
for i, row in enumerate(buttons):
    for j, button in enumerate(row):
        create_square_button(button, i + 1, j)

# Configure grid weight for resizing
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(1, len(buttons) + 1):
    root.grid_rowconfigure(i, weight=1)

# Run the application
root.mainloop()