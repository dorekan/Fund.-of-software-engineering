import re
from http.cookiejar import uppercase_escaped_char

text = str(input("Enter a string: "))
Readytext = re.sub(r'\s+', ' ',text)
word = re.split(r' ', Readytext)
abb = ""
for i in word:
    if len(i) >= 3:
        abb += str(i[0])
abb = abb.upper()
print(abb)
