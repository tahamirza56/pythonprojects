#Code written by Arsalan Bashir, in collaborations with Jibran and Taha on 09 October 2024 Bsc AI/ CS class!
maths = int(input("Enter marks obtained in Maths :"))
english = int(input("Enter marks obtained in english :"))
urdu  = int(input("Enter marks obtained in urdu :"))
social = int(input("Enter marks obtained in social :"))
science = int(input("Enter marks obtained in science :"))

total = maths + english + urdu + social + science
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
