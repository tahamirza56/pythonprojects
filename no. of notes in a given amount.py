amount= int(input("enter any amount:"))
if amount>=500:
    note_500= amount // 500
    print("no of 500rs notes", note_500)
    amount = amount - note_500 * 500
if amount>=200:
    note_200= amount//200
    print("no. of 200rs notes=", note_200)
    amount = amount - note_200 * 200
if amount>=100:
    note_100= amount // 100
    print("no. of 100rs notes=", note_100)
    amount = amount - note_100 * 100
if amount>= 50:
    note_50 = amount // 50
    print("no. of 50rs notes=", note_50);
    amount =amount - note_50 * 50
if amount>=20:
    note_20 = amount // 20
    print("no. of 20rs notes=", note_20)
    amount = amount - note_20 * 20
if amount>= 10:
    note_10 = amount // 10
    print("no. of 10rs notes=", note_10)
    amount = amount - note_10 * 10
if amount>=5:
    note_5 = amount // 5
    print("no. of 5rs notes=", note_5)
    amount = amount - note_5 * 5
if amount>=2:
    note_2 = amount // 2
    print("no. of 2rs notes=", note_2)
    amount = amount - note_2* 2
else:
    note_1= amount//1
    print("no. of 1rs notes=", note_1)
    amount= amount-note_1*1