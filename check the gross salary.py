basic_salary= int(input("enter salary amount:"))
if basic_salary <= 10000:
    hra= (20%100)*basic_salary
    da= (80%100)*basic_salary
    gross_salary= hra + da
    print("gross_salary:", gross_salary)
elif basic_salary<= 20000:
    hra2= (25%100)*basic_salary
    da2= (90%100)*basic_salary
    gross_salary2= hra2 + da2
    print("gross_salary:",gross_salary2 )
elif basic_salary > 20000:
    hra3= (30%100)*basic_salary
    da3= (95%100)*basic_salary
    gross_salary3= hra3 + da3
    print("gross_salary:", gross_salary3)