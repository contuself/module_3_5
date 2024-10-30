def get_multiplied_digits(number): #Напишите функцию get_multiplied_digits и параметр number в ней.
    str_number = str(number) #Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
    first = int(str_number[0]) #Создайте переменную first и запишите в неё первый символ из str_number в числовом представлении(int).
    if len(str_number) > 1: #если длина больше 1
        return first * get_multiplied_digits(int(str_number[1:])) #Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). 
    else: #иначе
        return first #вернуть оставшуюся цифру
result = get_multiplied_digits(40203) #переменная
print(result) #вывод на экран
