def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def run_program():
    num1 = 5
    num2 = 3

    sum_result = add(num1, num2)
    print(f"{num1} + {num2} = {sum_result}")
    
    mult_result = multiply(num1, num2)
    print(f"{num1} * {num2} = {mult_result}")

run_program()