import string
allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
error = str()
password = str(input("Введите пароль: "))
if len(password)!=8:
    error += "Неправильное количество символов \n"
if (any(symbol.isdigit() for symbol in password))==False:
    error += "Нет цифр \n"
if (any(symbol in string.ascii_uppercase for symbol in password)) == False:
    error += "Нет заглавных букв \n"
if (any(symbol in string.ascii_lowercase for symbol in password)) == False:
    error += "Нет строчных букв \n"
if (any(symbol in '*-#' for symbol in password)) == False:
    error += "Нет специальных знаков \n"
if (all(symbol in allowed for symbol in password))==False:
    error += "В пароле присутствуют недопустимые символы"
if error != '':
    print(error)
if error == '':
    print('Пароль установлен')





