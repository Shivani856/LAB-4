n= int(input("Enter the number : "))
a= 1
while n/a >= 10:
    a *= 10
while n!= 0:
    starting= n//a
    ending= n%10
    if starting != ending:
        print("This number is not a palindrome")
    else:
        print("This number is a palindrome")
    n= n%a//10
    a = a/100