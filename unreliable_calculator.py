import random
import sys
import math

def parse_string(u_input, operator):
    a,b = '',''
    running_a, running_b = True, True
    i = 0
    while running_a and i < u_input.find(operator):
        if u_input[i] in ['.','0','1','2','3','4','5','6','7','8','9']:
            a += u_input[i]
        elif u_input[i] == operator:
            a_running = False
        else:
            pass
        i += 1
        
    i = u_input.find(operator)
    
    while running_b and i < len(u_input):
        if u_input[i] in ['.','0','1','2','3','4','5','6','7','8','9']:
            b += u_input[i]
        elif u_input[i] == operator:
            b_running = False
        else:
            pass
        i += 1
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
    result += random.randint(-int(math.sqrt(abs(result))),int(math.sqrt(abs(result))))
    if result == a + b:
        result += random.randint(-2,2)
    while result < 0:
        result += math.sqrt(a)
    return result

def subtraction(a,b):
    result = a - b
    result += random.randint(-int(math.sqrt(abs(result))),int(math.sqrt(abs(result))))
    if result == a - b:
        result += random.randint(-2,2)
    return result

def multiplication(a,b):
    result = a * b
    result += random.randint(-int(math.sqrt(abs(result))),int(math.sqrt(abs(result))))
    if result == a * b:
        result += random.randint(-2,2)
    while result < 0:
        result += math.sqrt(a)
    return result

def division(a,b):
    result = a / b
    result += random.randint(-int(math.sqrt(abs(result))),int(math.sqrt(abs(result))))
    if result == a / b:
        result += random.randint(-2,2)
    while result < 0:
        result += math.sqrt(a)
    return result


while True:
    u_input = input('>>>')
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
