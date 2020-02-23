def is_float(text):
#def - это функция (её начало)
    if text.isalpha():
#.isalpha - содержит буквы
        return False
    try:
        float(text)
        return True
    except ValueError:
        return False


def get_number(text):
# def - это функция (её начало)
    if not is_float(text):
#is_float - название - провека переменной на возможность конвертирования в float
        print('Так у нас ничего не получится!')
        exit()
    return float(text)

if __name__ == '__main__':



    print('Привет, Катя! Я питонокалькулятор  :) ')
    print('\n')

    first = get_number(input("Напиши первое число:  "))

    znak = input('Что делаем? ("+", "-", "*", "/")  ' )

    if znak != "+" and znak != "-" and znak != "*" and znak != "/":
        print('Такого знака нет!')
        exit()

    second = get_number(input("Напиши второе число:  "))

    if second == 0 and znak == "/":
        print('Так нельзя!')
        exit()

    if znak == "+":
        c = first + second
        print( '\n')
        print('Результат: ' + str(c))

    elif znak == "-":
        c = first - second
        print( '\n')
        print('Результат: ' + str(c))

    elif znak == "*":
        c = first * second
        print( '\n')
        print('Результат: ' + str(c))

    elif znak == "/":
        c = first / second
        print( '\n')
        print('Результат: ' + str(c))

    print( '\n')
    print("Спасибо, что протестировала меня  :) ")

    input( )


