N=int(input("enter a number "))
sum=0
if N>0:
    while N>0:
        num=N%10
        sum+=num
        N=N//10
        print(sum)
else:
    print("enter a positive number")
