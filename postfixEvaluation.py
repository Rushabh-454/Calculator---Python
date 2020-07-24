import infixToPostfix as inToPost
from tkinter import messagebox

def evaluatePostfix(exp):
    stack = []

    for char in exp:
        if char not in ['+', '-', '*', '/']:
            stack.append(char)

        else:
            op2 = stack.pop()
            op1 = stack.pop()
            
            try:
                if char == '+':
                    stack.append(op1+op2)
                elif char == '-':
                    stack.append(op1-op2)
                elif char == '*':
                    stack.append(op1*op2)
                else:
                    stack.append(op1/op2)
            
            except ZeroDivisionError:
                messagebox.showerror("Error", "Division by zero!")
                return
    
    if len(stack) > 1:
        messagebox.showerror("Error", "Invalid Expression!")
        return
    
    return stack[0]