man = [5, 1 , 6 , 10 , 2, ]
print(man, " =  array")

print("----------------")

man.sort() # меняет оригинальный список
print(man, " =  sort man")

print("----------------")

sorted_man = sorted(man) # не меняет оригинальный список, а возвращает новый 
print(sorted_man, " = sorted man")

print("----------------")

man.reverse()
print(man, " = revers man")

print("----------------")

reversed_man = list(reversed(man))
print(reversed_man, " = reversed man")