def add(n1, n2):
    """adding n1 + n2"""
    return n1 + n2

def subtraction(n1, n2):
    """subtract n1 - n2"""
    return n1 - n2

def multiply(n1, n2):
    """multiply n1 * n2"""
    return n1 * n2

def division(n1, n2):
    """divide n1 with n2"""
    return n1 / n2


operations = {"+": add,
              "-": subtraction,
              "*": multiply,
              "/": division,
              }

calculator = True
repeat = False
saving_number = 0
while calculator:
    num1_int = 0
    if repeat == False:
        num1 = input("What first number do you want to calculate?: ")
        while not num1.isdigit():
            num1 = input("What first number do you want to calculate?: ")
        num1_int = int(num1)
    elif repeat == True:
        num1_int = saving_number

    operations_input = input("Which operation do you want?"
                             "\nType '+' for add"
                             "\nType '-' for subtract"
                             "\nType '*' for multiply"
                             "\nType '/' for division"
                             "\nYour input: ")
    while operations_input != "+" and operations_input != "-" and operations_input != "*" and operations_input != "/":
        operations_input = input("Which operation do you want?"
                                 "\nType '+' for add"
                                 "\nType '-' for subtract"
                                 "\nType '*' for multiply"
                                 "\nType '/' for division"
                                 "\nYour input: ")

    num2 = input("What second number do you want to calculate?: ")
    while not num2.isdigit():
        num2 = input("What second number do you want to calculate?: ")
    num2_int = int(num2)

    calculate = operations[operations_input]
    print(calculate(num1_int, num2_int))
    saving_number = (calculate(num1_int, num2_int))

    asking_again = input("Do you want calculate again with current result?"
                         "\n('yes' or 'no')"
                         "\n").lower()
    while asking_again != "yes" and asking_again != "no":
        asking_again = input("Do you want calculate again with current result?"
                             "\n('yes' or 'no')"
                             "\n").lower()

    if asking_again == "yes":
        repeat = True
    else:
        repeat = False
        asking_new = input("Do you want to start new calculation?"
                           "\n('yes' or 'no')"
                           "\n").lower()
        while asking_new != "yes" and asking_new != "no":
            asking_new = input("Do you want to start new calculation?"
                               "\n('yes' or 'no')"
                               "\n").lower()

        if asking_new == "no":
            calculator = False

