#written by taha mirza
num= int(input("enter any number:"))
if num % 5==0 and num % 11!= 0:
    print("number is divisible 5 but not by 11")
elif num % 5==0 and num % 11==0:
    print("number is divisible by both 5 and 11")
elif num % 5!=0 and num % 11==0:
    print("number is divisible is 11 but not 5")
else:
    print("neither divisible by 5 nor by 11")