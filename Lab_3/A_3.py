import sys
a = int(input("Предыдущее состояние счетчика: "))
b = int(input("Текущее состояние счетчика: "))
if a<10000 and b>=a:
    V = abs(b-a)
if a>9999:
    print("Неверное состояние счетчика")
    sys.exit()
if b<a:
    V = abs((10000-a)+b)
    
Price=float()
print("Использованно ", V)

if V<=300:
    Price=21
    print(round(Price, 2))
if V>300 and V<=600:
    Price=21+(V-300)*0.06
    print(round(Price, 2))
if V>600 and V<=800:
    Price=21+(300*0.06)+(V-600)*0.04
    print(round(Price, 2))
if V>800:
    Price = 21 + (300 * 0.06) + (200* 0.04) + (V-800)*0.025
    print(round(Price, 2))
Average = round((Price/V), 2)
print("Средняя цена за М^3", Average)
