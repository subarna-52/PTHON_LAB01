a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))

if a>b and a>c:
    max = a
    
elif b>a and b>c:
    max = b
    
else:
    max = c
    
print("Maximum number is: ", max)

