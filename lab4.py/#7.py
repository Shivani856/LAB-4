n= int(input("Enter a number: "))
x=0
y=1
z= 0
fib= 0
while x<n:
    fib= y+z
    y=z
    z= fib
    x= x+1
    print(fib)