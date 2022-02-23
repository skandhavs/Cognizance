num=int(input("Enter the number :"))
temp =num
rev=0
while num>0:
    rem=int(num%10)
    rev=rev*10+rem
    num=int(num/10)
if temp == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
