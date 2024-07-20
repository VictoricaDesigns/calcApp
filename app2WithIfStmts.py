# Content as of 5-10-2024
# insert shebang line here

print("Calculator App")

yourName = str(input("Enter your name: "))
print()
print("Hello, " + str(yourName) + ", let's calculate two numbers!")
print()
numberOne = int(input("Please enter your first number: "))
numberTwo = int(input("Please enter your second number: "))

print(""" 
Choices of Operator: 
+: Addition 
-: Subtraction 
/: Division 
%: Division with Remainder
*: Multiplication
^: Exponentiation
""")

op  = str(input("Enter Your Operator: "))

if op == "+":
    total = numberOne + numberTwo
elif op == "-":
    total = numberOne - numberTwo
elif op == "/":
    total = numberOne / numberTwo
elif op == "%":
    total = numberOne % numberTwo
elif op == "*":
    total = numberOne * numberTwo
elif op == "^":
    total = numberOne ^ numberTwo
else:
    print("You have entered an invalid choice. Exit the program then try again.")


print()
print("Awesome, " + yourName + ", Your answer is..." + str(total) + ".")
print("Thank you and have a great day!")
