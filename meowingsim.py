def calculadora(a,b,c):
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print(a/c)
        if c != 0:
            print(a/c)
        else:
            print("erm actually dividing by zero is not possible so sybau")
    else: 
        print("erm you didnt write anything possible for an operation. enter either + - * /")
try:
    a = int(input("enter the first number "))
    b = input("Enter the operation ").strip()
    c = int(input("Enter thse second number "))
except ValueError:
    print("Something went wrong")
calculadora(a, b, c)

print("bruh")
print("does this work")
