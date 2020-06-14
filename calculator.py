"""This is a calculator program"""

print("This is a Calculator Program")
OPTION = 0
while OPTION != 5:
    print("Option 1 - add")
    print("Option 2 - subtract")
    print("Option 3 - multiply")
    print("Option 4 - divide")
    print("Option 5 - quit program")
    print(" ")
    OPTION = input("Enter option:")
    if OPTION == 1:
        add1 = input("Enter first value:")
        add2 = input("Enter second value:")
        print(add1, "+", add2, "=", add1 + add2)
        print(" ")
    elif OPTION == 2:
        sub1 = input("Enter first value:")
        sub2 = input("Enter second value:")
        print(sub1, "-", sub2, "=", sub1 - sub2)
        print(" ")
    elif OPTION == 3:
        mul1 = input("Enter first value:")
        mul2 = input("Enter second value:")
        print(mul1, "*", mul2, "=", mul1 * mul2)
        print(" ")
    elif OPTION == 4:
        div1 = input("Enter first value:")
        div2 = input("Enter second value:")
        print(div1, "/", div2, "=", div1 / div2)
        print(" ")
    elif OPTION == 5:
        print("This program has ended")
    else:
        print("Invalid input")
        print(" ")
print("Thank you for using the Calculator Program")
