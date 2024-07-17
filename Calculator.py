print("For operations '+','-','*','/' and '%' enter your choice as 1\n ")
print("For operations '**','^' enter your choice as 2\n")
print("Note:'%' is for finding remainder when second operand divides the first operand\n")
print("Note:'**' for finding square of a required number\n")
print("Note:'^' for finding nth power of a required number\n")
n=int(input("Enter your choice:"))
if(n==1):
    a=int(input("Enter first operand:"))
    b=int(input("Enter second operand:"))
    operation_choice1=input("Enter the operation(+,-,*,/,%):")

    if(operation_choice1=="+"):
        print("Sum=",a+b)
    elif(operation_choice1=="-"):
        print("Difference=",a-b)
    elif(operation_choice1=="*"):
        print("Product=",a*b)
    elif(operation_choice1=="/"):
        print("Result=",a/b)
    elif(operation_choice1=="%"):
        print("Remainder=",a%b)
    else:
        print("Invalid Operator\n")
elif(n==2):
    c=int(input("Enter the operand for square or for nth power:"))
    operation_choice2=input("Enter the operation(**,^):")
    if(operation_choice2=="**"):
        print("square of a given number:",c*c)
    elif(operation_choice2=="^"):
        power=int(input("Enter the power to be raised for the entered number:"))
        print("result=",c**power)
    else:
        print("Invalid Operator\n")
else:
    print("Invalid Choice\n")
