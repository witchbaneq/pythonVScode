is_ok = False

while not is_ok:
    try:
        number = int(input("Введите число: "))
        is_ok = True
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")

print(number)
