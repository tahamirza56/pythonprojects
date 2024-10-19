n= int(input("any 5 digit number:"))
r= n % 10
rev= r
n= n//10
r= n%10
rev2= rev*10+r
n= n//10
r= n%10
rev3= rev2*10+r
n= n//10
r= n%10
rev4= rev3*10+r
n= n//10
r= n%10
rev5= rev4*10+r
print(rev5)