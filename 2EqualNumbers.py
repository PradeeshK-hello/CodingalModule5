def checkifSame(number1,number2):
    if ((number1 ^ number2) != 0):
        print("Numbers are not equal.")
    else:
        print("Both numbers are equal.")
number1 = int(input("Enter the first number to compare: "))
number2 = int(input("Enter the second number to compare: "))
checkifSame(number1,number2)