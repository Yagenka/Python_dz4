# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности

my_number = input('Задайте через пробел последовательность чисел - ')
my_list = my_number.split()

for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

my_new_list = []

for i in my_list:
    count = 0
    for j in my_list:
        if i == j:
            count += 1
    if count == 1:
        my_new_list.append(i)


print(f'Список неповторяющихся элементов исходной последовательности - {my_new_list}')