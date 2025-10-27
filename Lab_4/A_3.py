list = str(input("Введите нули и единицы: "))
loose = 0
strick = 0
Nstrick = 0
for i in list:
    if len(list) < 5:
        print("Ошибка, введено неправильное значение!")
        break
    if i != "0" and i != "1":
        print("Ошибка, введено неправильное значение!")
        break
    if i == "0":
        loose += 1
        Nstrick += 1
    if i == "1":
        Nstrick = 0
    if strick < Nstrick:
        strick = Nstrick
L = round(loose/len(list)*100, 1)
if L < 1 :
    quality = "Отличное качество"
if L> 1 and L <= 5 :
    quality = "Хорошее качество"
if L> 5 and L < 10 :
    quality = "Удовлетворительное качество"
if L >= 10 and L <= 20 :
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"
print("Общее кол-во пакетов -", len(list))
print("Количество потерь -", loose)
print("Самая длинна последовательность потерь - ", strick)
print("Процент потерь -",L,"%")
print("Состояние сети -", quality)