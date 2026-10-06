import math
print("\t___CALCULATOR___")

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a*b

def div(a,b):
    if b == 0:
        print("\nYou cannot divide by zero! ")
    else:
        q = a/b 
        r = a%b
        print("\nThe quotient is : %s" %q)
        print("\nThe remainder is %s" %r)

def sqr(a):
    if a < 0 :
        print("\nCannot calculate the square root of negative number")
        return None
    else:
        x = math.sqrt(a)
    return x
while(True):
    print("\n\nChoose the operation you want to perform: ")
    print("\n\t1.ADDITION")
    print("\n\t2.SUBTRACTION")
    print("\n\t3.MULTIPLICATION")
    print("\n\t4.DIVISION")
    print("\n\t5.SQUARE ROOT")
    print("\n\t6.EXIT")

    choice = int(input(">"))

    if choice == 1:
        print("\n\nEnter the two number: ")
        num1 = int (input(">"))
        num2 = int (input(">"))
        s = add(num1, num2)
        print("The sum is : %s" %s)

    elif choice == 2 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(">"))
        num2 = int(input(">"))
        m = sub(num1, num2)
        print("\nThe difference is: %s" %m)

    elif choice == 3 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(">"))
        num2 = int(input(">"))
        p = mul(num1,num2)
        print("\nThe product is: %s" %p)

    elif choice == 4 :
        print("\n\nEnter the two numbers: ")
        num1 = int(input(">"))
        num2 = int(input(">"))
        div(num1,num2)

    elif choice == 5 :
        print("\n\nEnter the number: ")
        num1 = int(input(">"))
        r = sqr(num1)
        if r is not None:
            print("\nThe square root is: %s" %r)

    elif choice == 6:
        print("\nYou chose to exit. Bye..........")
        break

    else:
        print("\nplease choose a valid number from 1 to 6.")
        


