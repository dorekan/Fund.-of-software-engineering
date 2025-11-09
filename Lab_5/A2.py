import re
text = str(input("Enter a string: "))
sentence = re.split(r'(?<=[.?!]) ', text)
x = 0
for i in sentence:
    print(re.sub(r'\s+', ' ',i.strip()))
    x +=1
print("Преложений в тексте -",x)
