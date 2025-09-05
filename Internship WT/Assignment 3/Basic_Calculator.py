# 2.Basic Calculator – Create a program that performs addition, subtraction, multiplication, and division based on user input

def calculator():
    num1 = int(input("Enter value for num1 :"))
    num2 = int(input("Enter value for num2 :"))

    ### MENU ####
    print("\nChoose operation to perform:")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter Your Choice :")

    if choice == '1':
        print("Addition is:", num1 + num2)
    elif choice == '2':
        print("Substraction is :", num1 - num2)
    elif choice == '3':
        print("Multiplication is :", num1*num2)
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero not allowed.")
    else:
        print("Please Enter Valid Choice!!")


calculator()
