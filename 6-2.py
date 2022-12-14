# Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


import random

number = int(input("Введите число N: "))
list = [random.randint(0, 10) for i in range(0,number)]
print(f"Cписок из {number} чисел: \n{list}")

list2 = []
for i in range ( 0, ((len(list) + 1)//2) ): list2.append(list[i] * list[-1-i]) 
print(f"Результат: \n{list2}")