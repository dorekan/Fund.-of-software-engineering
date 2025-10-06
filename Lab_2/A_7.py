x1 = int(input("x1 "))
y1 = int(input("y1 "))

x2 = int(input("x2: "))
y2 = int(input("y2: "))

clr1 = (x1+y1)%2
clr2 = (x2+y2)%2

if clr1 == clr2:
    print("YES")
    if clr1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")