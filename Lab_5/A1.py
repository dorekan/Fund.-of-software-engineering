text = str(input("Enter a string: "))
while True:
    Lposition = text.find("(")-1
    Rposition = text.find(")")
    text = text.replace(text[Lposition:Rposition+1],"")
    if Rposition == -1:
        break
print(text)