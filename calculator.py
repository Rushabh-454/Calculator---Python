from tkinter import *
import infixToPostfix as inToPost
import postfixEvaluation as postEval
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Calculator')
img = ImageTk.PhotoImage(Image.open('calculator.png'))
root.iconphoto(False, img)

e = Entry(root, width=50, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(character):
    operators = ['+', '-', '*', '/']
    current = e.get().split()
    flag = True

    if character == '(':
        if current == []:
            character = '('
        else:
            if current[-1] not in operators + ['.', '(']:
                character = ''
                flag = False

    if character == ')' and '(' not in current:
        character = ''
        flag = False

    if character in operators:
        if current == [] or current[-1] in operators:
            character = ''
            flag = False
            
    if character == '.':
        if current == []:
            character = '.'
        elif '.' in current[-1]:
            character = ''
        flag = False

    current = e.get()
    e.delete(0, END)

    if character in operators + ['(', ')'] and flag:
        character = ' ' + character + ' '

    e.insert(0, current+character)

def button_equal():
    infix = e.get().split()
    print(infix)
    
    bracket = 0
    for char in infix:
        if char == '(':
            bracket += 1
        elif char == ')':
            bracket -= 1
        if bracket < 0:
            messagebox.showerror("Error", "Invalid Expression!")
            return 
    
    if bracket != 0:
        messagebox.showerror("Error", "Invalid Expression!")
        return 

    expresssion = inToPost.infixToPostfix(infix)
    ans = postEval.evaluatePostfix(expresssion)
    
    if ans is not None:
        e.delete(0, END)
        e.insert(0, ans)

def button_back():
    current = e.get().split()
    e.delete(0, END)
    e.insert(0, "".join(current[:-1]))

def button_clear():
    e.delete(0, END)

myFont = tkFont.Font(family='Helvetica', size=17)

button_1 = Button(root, text="1", padx=28, pady=5, font=myFont, command=lambda: button_click("1"))
button_2 = Button(root, text="2", padx=28, pady=5, font=myFont, command=lambda: button_click("2"))
button_3 = Button(root, text="3", padx=28, pady=5, font=myFont, command=lambda: button_click("3"))
button_4 = Button(root, text="4", padx=28, pady=5, font=myFont, command=lambda: button_click("4"))
button_5 = Button(root, text="5", padx=28, pady=5, font=myFont, command=lambda: button_click("5"))
button_6 = Button(root, text="6", padx=28, pady=5, font=myFont, command=lambda: button_click("6"))
button_7 = Button(root, text="7", padx=28, pady=5, font=myFont, command=lambda: button_click("7"))
button_8 = Button(root, text="8", padx=28, pady=5, font=myFont, command=lambda: button_click("8"))
button_9 = Button(root, text="9", padx=28, pady=5, font=myFont, command=lambda: button_click("9"))
button_0 = Button(root, text="0", padx=28, pady=5, font=myFont, command=lambda: button_click("0"))

button_add = Button(root, text="+", padx=28, pady=5, font=myFont, command=lambda: button_click("+"))
button_sub = Button(root, text="-", padx=30, pady=5, font=myFont, command=lambda: button_click("-"))
button_mul = Button(root, text="*", padx=30, pady=5, font=myFont, command=lambda: button_click("*"))
button_div = Button(root, text="/", padx=30, pady=5, font=myFont, command=lambda: button_click("/"))
button_decimal = Button(root, text=".", padx=31, pady=5, font=myFont, command=lambda: button_click("."))
button_equal = Button(root, text="=", padx=28, pady=5, font=myFont, command=button_equal)

button_open = Button(root, text="(", padx=30, pady=5, font=myFont, command=lambda: button_click("("))
button_close = Button(root, text=")", padx=31, pady=5, font=myFont, command=lambda: button_click(")"))

button_back = Button(root, text="<<", padx=22, pady=6, font=myFont, command=button_back)
button_clear = Button(root, text="C", padx=28, pady=5, font=myFont, command=button_clear)

button_clear.grid(row=1, column=0)
button_open.grid(row=1, column=1)
button_close.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_mul.grid(row=2, column=3)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_add.grid(row=4, column=3)

button_back.grid(row=5, column=0)
button_0.grid(row=5, column=1)
button_decimal.grid(row=5, column=2)
button_equal.grid(row=5, column=3)

root.mainloop()