def function():

    print("1.Capitalize string")
    print("2.count")
    print("3.replace string")
    print("4.title")

    x = input("Enter num between 1-4: ")

    if x not in ['1','2','3','4']:
        print("Invalid input")
        return

    a = input("Enter string here: ")

    if x == '1':
        print("Capitalize string is: ",a.capitalize())

    elif x == '2':
        j = input("Enter what whould you count: ")
        print(j, "is in string",a.count(j),"times")

    elif x == '3':
        y = input("Enter what you chang in string: ")
        z = input("Enter what with you chang: ")
        print("New string is:",a.replace(y,z))

    elif x == '4':
        print("Title string is: ",a.title())
function()