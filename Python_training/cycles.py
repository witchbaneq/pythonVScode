array = [1, 2, 3, 4, 5]

for i in array:
    print(i)

man = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

for i in man:
    print(man[i]) # выводит значения словаря

for i in  man:
    print(i) # выводит ключи словаря 

for i in range(100):
    print(i)

for i in range(0, 20, 2): # 0 - начальное значение, 20 - конечное значение, 2 - шаг
    print(i)  # выводит четные числа от 0 до 20

password = ""
while password != "1234":
    password = input("Enter password: ")
    if password == "1234":
        print("Пароль верный")
    else:
        print("Пароль неверный, попробуйте еще раз")

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in array[0:11:2]: # 0 - начальное значение, 11 - конечное значение, 2 - шаг
    print(i)