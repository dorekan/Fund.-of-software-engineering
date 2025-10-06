a = int(input("Введите первое число 1-1000 "))
b = int(input("Введите второе число 1-1000 "))
if a>=1 and a<=1000 and b>=1 and b<=1000:
    result = [a, b][a <= b]
    print(result, " больше")
else:
    print("Неправильное значение переменных")