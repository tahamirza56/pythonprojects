#Code written by taha mirza
maths = int(input("Enter marks obtained in Maths :"))
physics = int(input("Enter marks obtained in physics :"))
computer = int(input("Enter marks obtained in computer :"))
chemistry= int(input("Enter marks obtained in chemistry :"))
biology = int(input("Enter marks obtained in biology :"))

total = maths + physics + computer + chemistry + biology
percentage = total/500*100

if percentage >= 33 :
        print(f"Pass with {percentage} %")
        if percentage >= 90 :
            print("Grade A")
        elif percentage >= 80 :
            print("Grade B")
        elif percentage >= 70 :
            print("Grade C")
        elif percentage >= 60 :
            print("Grade D")
        elif percentage >= 50 :
            print("Grade E")
        elif percentage >= 40 :
            print("Grade F")
        elif percentage >= 33 :
            print("Sharm kro beta isk aage grade hee nhi rahy.")
else :
    print(f"Failed with {percentage} %")
