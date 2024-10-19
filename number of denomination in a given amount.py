notes = [500,200,100,50,20,10,5,2,1]

amount = int(input("Enter Amount to be paid : "))

for Count in notes:
    count = amount//Count
    print("Note Value : ", '\tnumber of notes ',count)
    amount = amount%Count