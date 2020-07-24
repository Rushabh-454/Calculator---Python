
top = -1
array = [] 
output = [] 
precedence = {'+':1, '-':1, '*':2, '/':2} 
	
def isEmpty(): 
    global top
    return True if top == -1 else False

def peek(): 
    return array[-1] 

def pop():
    global top 
    if not isEmpty(): 
        top -= 1
        return array.pop() 
    else: 
        return "$"

def push(op): 
    global top
    top += 1
    array.append(op) 

def isOperand(ch): 
    if ch not in ['+', '-', '*', '/', '(', ')']:
        return True
    return False 

def notGreater(i): 
    try: 
        a = precedence[i] 
        b = precedence[peek()]
        return True if a <= b else False
    except KeyError: 
        return False
        
def infixToPostfix(exp): 
    
    for i in exp: 
        if isOperand(i):
            if '.' in i: 
                output.append(float(i))
            else:
                output.append(int(i))
        
        elif i == '(': 
            push(i) 

        elif i == ')': 
            while((not isEmpty()) and peek() != '('): 
                a = pop() 
                output.append(a) 
            if (not isEmpty() and peek() != '('): 
                return -1
            else: 
                pop() 

        else: 
            while(not isEmpty() and notGreater(i)): 
                output.append(pop()) 
            push(i) 

    while not isEmpty(): 
        output.append(pop()) 

    return output

