#code written by taha mirza
base_salary = int(input("Enter the Salary/month :"))
dearmin_allowance = 30 / 100 * base_salary
hra = 10 / 100 * base_salary
ta = 5 / 100 * base_salary
ctc_salary = base_salary + dearmin_allowance + hra + ta
print("ctc_salary :", ctc_salary)
if ctc_salary < 250000:
    print("No Tax")
elif ctc_salary > 250000 and ctc_salary < 600000:
        tax1= (5/100*(ctc_salary - 250000))
        salary_after_tax_1= ctc_salary - (5/100*(ctc_salary - 250000))
        print("total_tax:", tax1)
        print("salary_after_tax_1:", salary_after_tax_1)
elif ctc_salary > 600000 and ctc_salary < 900000 :
        tax2= (10/100*(ctc_salary - 250000))
        salary_after_tax_2= ctc_salary - (10/100*(ctc_salary - 250000))
        print("total_tax:", tax2)
        print("salary_after_tax_2:", salary_after_tax_2)
elif ctc_salary >900000 and ctc_salary < 1200000 :
        tax3= (15/100*(ctc_salary - 250000))
        salary_after_tax_3= ctc_salary - (15/100*(ctc_salary - 250000))
        print("total_tax:", tax3)
        print("salary_after_tax_3:", salary_after_tax_3)
elif ctc_salary >1200000 and ctc_salary < 1500000 :
        tax4= (20/100*(ctc_salary - 250000))
        salary_after_tax_4= ctc_salary - (20/100*(ctc_salary - 250000))
        print("total_tax:", tax4)
        print("salary_after_tax_4:", salary_after_tax_4)
elif ctc_salary > 1500000:
    tax5= (30/100*(ctc_salary - 250000))
    salary_after_tax_5= ctc_salary - (30/100*(ctc_salary - 250000))
    print("total_tax:", tax5)
    print("salary_after_tax_5:", salary_after_tax_5)
