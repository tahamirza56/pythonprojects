char= input("enter any character:")
if char.isalpha():
    print("char is an alphabet")
elif char.isdigit():
    print("char is a digit")
elif char.isprintable():
    print("char is a special character")