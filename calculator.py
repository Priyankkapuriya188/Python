def calculator():

    print("1.Addition (+)")
    print("2.Subtraction (-)")
    print("3.Multiplication (*)")
    print("4.Division (/)")
    print("5.Floor division (//)")
    print("6.Exponentiation (**)")
    print("7.Modulus (%)")

    c = input("Enter num between 1-7: ")

    if c not in ['1','2','3','4','5','6','7']:
        print("Invalid input")
        return

    try:
        a = int(input("Enter a first num: "))

        if c in ['1','2','3','4','5','7']:
            b = int(input("Enter a second num: "))

        elif c in ['6']:
            i = int(input("Enter power: "))

    except ValueError:
            print("Enter numeric values: ")
            return

    if c == '1':
        print("The result is: ",a+b)
    elif c == '2':
        print("The result is: ",a-b)
    elif c == '3':
        print("The result is: ",a*b)
    elif c == '4':
        if b == 0:    
            print("Division by zero is not allowed")
        else :
            print("The result is: ",a/b)
    elif c == '5':
        print("The result is: ",a//b)
    elif c == '6':
        print("The result is: ",a**i)
    elif c == '7':
        print("The result is: ",a%b)

calculator()