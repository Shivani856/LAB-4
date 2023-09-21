a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
D= (b**2)-(4*a*c)
R1= (-b +(D**0.5))/2*a
R2= (-b -(D**0.5))/2*a
if D>0:
    print("Roots are", round(R1,2),ROUND(R2,2))
elif D<0:
    print("NO REAL ROOTS")
else:
    print("ROOTS ARE EQUAL",R1)