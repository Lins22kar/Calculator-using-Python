print("**********Calculator**********")
print('\n')

num1=float(input("Enter a first number "))
num2=float(input("Enter a second number "))

print(" Press 1 for Addition\n Press 2 for Subtraction\n Press 3 for Multiplication\n Press 4 for Division\n Press 0 to Quit\n")

Entered_number=int(input("Enter You Choice "))

if Entered_number==1:
    print("Addition of Two numbers are: ",num1+num2)
elif Entered_number==2:
    print("Subtraction of Two numbers are: ",num1-num2)
elif Entered_number==3:
    print("Multiplication of Two numbers are: ",num1*num2)
elif Entered_number==4:
    print("Division of Two numbers are: ",num1/num2)
elif Entered_number==0:
    print("Bye Bye...Have a Great Day")
else:
    print("Please enter a valid input")
