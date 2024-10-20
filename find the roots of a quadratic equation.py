def quadratic_equation(a, b, c, x):
    return a*x**(2) + b*x + c
a = float(input("enter coefficient a:"))
b = float(input("enter coefficient b:"))
c = float(input("enter coefficient c:"))
D= (b**(2) - (4*a*c))**(1/2)
root1= (-b + D)/ (2*a)
root2= (-b - D)/ (2*a)
print("root1:", root1)
print("root2:" ,root2)
x = root1 or root2
result = a*x**(2) + b*x + c
print(f"the value of quadratic_equation for the value of x={x} is", result)