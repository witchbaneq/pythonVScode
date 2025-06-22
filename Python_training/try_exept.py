is_ok = False

while not is_ok:
    try:
        number = int(input("Введите число: "))
        is_ok = True
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")

print(number)


def divide(a, b): # Функция для деления двух чисел
    result = a / b
    return result

good = False
while not good: # Цикл для повторного запроса ввода в случае ошибки
    try:
        result = divide(int(input("Введите делимое: ")), int(input("Введите делитель: ")))
        print(result)
        good = True
    except (ZeroDivisionError, ValueError):
        print("Ошибка ввода, попробуйте еще раз")