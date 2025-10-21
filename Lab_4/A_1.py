import random
import time
N = int(input("Количество примеров: "))
tAnsw = 0
summTime = 0
for i in range(N):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    print("Пример ",i,"/",N)
    while True:
        try:
            sTime = time.time()
            answ = int(input(f"{a}*{b}="))
            uTime = round(time.time() - sTime, 1)

            break
        except ValueError:
            print("Введите цеолое число!")
    if answ==a*b:
        print("Верно!, Затраченное время - ", uTime, " сек")
        tAnsw = tAnsw+1
        summTime += uTime
    else:
        print("Неверно!, Затраченное время - ", uTime, " сек")
        summTime += uTime
    i+=1
print("Общее затраченное время: ", summTime)
print("Решены правильно - ", tAnsw, "/", N)
print("Среднее время на вопрос - ", summTime/N, " сек")
print("Процент правильных ответов - ", round(tAnsw/N*100), "%")


