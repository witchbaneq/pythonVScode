man = [5, 1 , 6 , 10 , 2, ]
print(man, " =  array")

print("----------------")

man.sort()
print(man, " =  sort man")

print("----------------")

sorted_man = sorted(man)
print(sorted_man, " = sorted man")
# The sorted() method does not modify the original list, it returns a new sorted list.

print("----------------")

man.reverse()
print(man, " = revers man")

print("----------------")

reversed_man = list(reversed(man))
print(reversed_man, " = reversed man")