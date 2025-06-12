man = [5, 1 , 6 , 10 , 2,]
print(man, " =  array")

print("----------------")

man.sort() # меняет оригинальный список
print(man, " =  sort man")

print("----------------")

man_0 = [5, 1 , 6 , 10 , 2,]
sorted_man_0 = sorted(man_0) # не меняет оригинальный список, а возвращает новый
print(sorted_man_0, " = sorted man_0")

print("----------------")

man_1 = [5, 1 , 6 , 10 , 2,]
man_1.reverse() # меняет оригинальный список
print(man_1, " = revers man_1")

print("----------------")

man_2 = [5, 1 , 6 , 10 , 2,]
reversed_man_2 = list(reversed(man_2)) # не меняет оригинальный список, а возвращает новый
print(reversed_man_2, " = reversed man_2")

print("----------------")

array = [1, 2, 3, 4, 5]
array.pop() # удаляет последний элемент из списка
print(array)
array.append(7)  # добавляет элемент в конец списка
print(array)
array.pop(4) # удаляет элемент по индексу
print(array)
array.insert(2, 8) # вставляет элемент по индексу
print(array)
array.remove(8) # удаляет элемент по значению
print(array)
