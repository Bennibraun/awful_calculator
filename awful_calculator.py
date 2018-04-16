import random
import sys


def parse_string(u_input, operator):
    a,b = '',''
    running_a, running_b = True, True
    i = 0
    while running_a:
        if u_input[i] in [' ',operator]:
            running_a = False
        else:
            a += u_input[i]
        i += 1
    i = len(u_input)-1
    
    while running_b:
        if u_input[i] in [' ',operator]:
            running_b = False
        else:
            b += u_input[i]
        i -= 1
    a = float(a)
    b = float(b)
    if operator == '+':
        print(addition(a,b))
    elif operator == '-':
        print(subtraction(a,b))
    elif operator == '*':
        print(multiplication(a,b))
    elif operator == '/':
        print(division(a,b))
                  


def addition(a,b):
    result = a + b
    if abs(result) > 150:
        result += random.randint(-13,13)
    elif abs(result) > 70:
        result += random.randint(-7,7)
    else:
        result += random.randint(-1,1)
    return result

def subtraction(a,b):
    result = a + b
    if abs(result) > 150:
        result += random.randint(-13,13)
    elif abs(result) > 70:
        result += random.randint(-7,7)
    else:
        result += random.randint(-1,1)
    return result

def multiplication(a,b):
    result = a * b
    if abs(result) > 1000:
        result += random.randint(-75,75)
    elif abs(result) > 100:
        result += random.randint(-20,20)
    elif abs(result) > 50:
        result += random.randint(-5,5)
    else:
        result += random.randint(-2,2)
    return result

def division(a,b):
    result = a / b
    if abs(result) > 1000:
        result += random.randint(-75,75)
    elif abs(result) > 100:
        result += random.randint(-20,20)
    elif abs(result) > 50:
        result += random.randint(-5,5)
    else:
        result += random.randint(-2,2)
    return result


while True:
    u_input = input('')
    if u_input == 'exit' or u_input == 'stop' or u_input == 'quit':
        sys.exit()
    elif '+' in u_input:
        parse_string(u_input,'+')
    elif '-' in u_input:
        parse_string(u_input,'-')
    elif '*' in u_input:
        parse_string(u_input,'*')
    elif '/' in u_input:
        parse_string(u_input,'/')
    else:
        print('Please use a valid operator (+,-,*,/).')
