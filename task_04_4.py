# Задана натуральная степень k.
# Сформировать случайным образом
# список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

 
from random import randint

k = int(input("Задайте натуральную степень - "))

list_n = []

for i in range(k+1):
    list_n.append(randint(0, 100))
print(f'Список коэффициентов - {list_n}')

polinom = ''
while k >= 0:
     for n in list_n:
         if n > 1:
           if k > 1:
              polinom += str(n) + '*x^'+ str(k) + ' + '
           if k == 1:
              polinom += str(n) + '*x' 
           if k == 0:
              polinom += ' + '+ str(n) 
         if n == 1:
            if k > 1:
               polinom += 'x^'+ str(k) + ' + '
            if k == 1:
               polinom += 'x' 
            if k == 0:
               polinom += ' + '+ str(n) 
         k -= 1
polinom += ' = 0'
    
print (polinom) 

with open('file.txt', 'w') as data:
 data.write(polinom)





