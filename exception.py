import sys



try: 
    x = int(input("Enter value of x :"))
    y = int(input ("Enter value of y :"))
except ValueError:
    print("integer Value is allowed only ")
else:
    print("minus number not allow")
    sys.exit(1)
try: 
    resualts = x / y
except ZeroDivisionError:
    print("zero can not divide to number ")
    sys.exit(1)


print(resualts)