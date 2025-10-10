a = int(input("Предыдущее состояние счетчика: "))
b = int(input("Текущее состояние счетчика: "))
V = b-a
Price=float()
print("Использованно ", V)

if V<=300:
    Price=21
    print(Price)
if V>300 and V<=600:
    Price=21+(V-300)*0.06
    print(Price)
if V>600 and V<=800:
    Price=21+(300*0.06)+(V-600)*0.04
    print(Price)
if V>800:
    Price = 21 + (300 * 0.06) + (200* 0.04) + (V-800)*0.025
    print(Price)
