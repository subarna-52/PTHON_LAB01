n = int(input("ENter a number: "))
if n<2:
    print("It is not a prime number.")
    
for i in range(2,n):
    if n%i==0:
        print("It is not a prime number.")
        break
        
    else:
        print("It is a prime number.")