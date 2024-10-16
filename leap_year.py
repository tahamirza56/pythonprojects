year = int(input("Enter a year to check :"))
if year % 100 != 0 and year % 4 == 0 or year % 400 == 0:
        print("Leap Year")
else :
        print("Not a Leap Year")


