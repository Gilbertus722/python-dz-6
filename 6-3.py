#Сформировать список из N членов последовательности.
#Для N = 5: 1, -3, 9, -27, 81 и т.д.

number = int(input("Введите число N: "))
lst = [(-3)**i for i in range(number)]
print(f"Список из {number} чисел: {lst}")