a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a <= b and a <= c:
    print("Smallest =", a)
elif b <= a and b <= c:
    print("Smallest =", b)
else:
    print("Smallest =", c)