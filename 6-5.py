# Есть список случайных чисел в промежутке от 1 до 100, количеством 200. 
# Создайте список кортежей, первый элемент которого - индекс элемента, 
# а второй - сам элемент, при условии, что они не совпадают.
#[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

import random

numbers = [random.randint(1, 100) for _ in range(200)]
print(f'Cписок двухсот: {list(enumerate(numbers))}')

print(f'Список без совпадений -> {list(filter(lambda i: i[0] != i[1], enumerate(numbers)))}')