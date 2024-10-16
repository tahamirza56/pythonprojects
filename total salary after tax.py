base_salary = int(input("Enter the Salary/month :"))
dearmin_allowance = 30 / 100 * base_salary
hra = 10 / 100 * base_salary
ta = 5 / 100 * base_salary
ctc_salary = base_salary + dearmin_allowance + hra + ta
print("ctc_salary :", ctc_salary)
if ctc_salary < 250000:
    print("No Tax")
elif ctc_salary > 250000 and ctc_salary < 600000:
        tax1= (ctc_salary - 250000) - (5/100*(ctc_salary - 250000))
        print("after tax:", tax1)
elif ctc_salary < 900000 :
        tax2= (ctc_salary - 250000)- (10/100*(ctc_salary - 250000))
        print("after tax:", tax2)
elif ctc_salary < 1200000 :
        tax3= (ctc_salary - 250000) - (15/100*(ctc_salary - 250000))
        print("after tax:", tax3)
elif ctc_salary < 1500000 :
        tax4= (ctc_salary - 250000) - (20/100*(ctc_salary - 250000))
        print("after tax:", tax4)
else :
    tax5= (ctc_salary - 250000)- (30/100*(ctc_salary - 250000))
    print("after tax:", tax5)
