# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def coefficient (polinom_1: list):
    coef_0 = 0
    coef_1 = 0
    coef_2 = 0
    coef_3 = 0
    for y in polinom_1:
       if '= 0' in y:
        l = len(y)
        coef_0 = y[0:(l-4)]
       if '*x' in y:
        l = len(y)
        coef_1 = y[0:(l-3)]
       if '*x^2' in y:
        l = len(y) 
        coef_2 = y[0:(l-5)]
       if '*x^3' in y:
        l = len(y)
        coef_3 = y[0:(l-5)]
    my_list = [coef_3, coef_2, coef_1, coef_0]
    for i, item in enumerate(my_list):
       my_list[i] = int(item)
    return (my_list)

with open('file_1.txt', 'r') as data:
 read_line_1 = data.read()
print(f'Первый многочлен: {read_line_1}')
polinom_1 = read_line_1.split('+')
my_list_1 = coefficient (polinom_1)

with open('file_2.txt', 'r') as data:
 read_line_2 = data.read()
print(f'Второй многочлен: {read_line_2}')
polinom_2 = read_line_2.split('+')
my_list_2 = coefficient (polinom_2)

summa = map(sum, zip(my_list_1,my_list_2))
summa = list(summa)
for i, item in enumerate(summa):
    summa[i] = str(item)
summa_str = summa[0] + '*x^3 + ' + summa[1] + '*x^2 + ' + summa[2] + '*x + ' + summa[3] + ' = 0' 
print(f'Сумма многочленов: {summa_str}')

with open('file_3.txt', 'w') as data:
 data.write(summa_str)







