# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности

my_number = input('Задайте через пробел последовательность чисел - ')
my_list = my_number.split()

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

my_set = set(my_list)
my_new_list = list(my_set)
print(f'Список неповторяющихся элементов исходной последовательности - {my_new_list}')