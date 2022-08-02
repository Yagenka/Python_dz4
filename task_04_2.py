# Задайте натуральное число N.
# Напишите программу,
# которая составит список простых множителей числа N.

n = int(input("Задайте натуральное число - "))   

def get_simple_miltipliers(n: int):
   i = 2
   my_list = []
   while i <= n:
       while n % i == 0:
           my_list.append(i)
           n //= i           
       i += 1
   return my_list

my_simple_miltipliers = get_simple_miltipliers (n)
print(f'Список простых множителей для {n} - {my_simple_miltipliers}')

