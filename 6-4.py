# 4 - Дан список случайных чисел. Оставьте только те, сумма цифр которых четна

import random

def Random_list (length_list, down_border, up_border):
    rand_list=[]
    for i in range(0,length_list):
        rand_list.append(random.randint(down_border,up_border))
    return rand_list


print()
number=int(input('Размер списка: '))
source_list=[]
source_list=Random_list(number, 10, 100)
print('Исходный список')
print(source_list)
result_list=[source_list[i] for i in range(len(source_list)) if (source_list[i]//10+source_list[i]%10)%2==0]
print('Результат: ')
print(result_list)