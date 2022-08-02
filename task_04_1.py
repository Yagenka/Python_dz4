# Вычислить число π c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141     10^(-10) <= d <= 10^(-1)

import math 

def num_after_point (d: float):
    count = 0
    while d != 1:
        d *= 10
        count += 1
    return count

d = float(input("Задайте точность в пределах от 0.1 до 0.0000000001 - "))
number = num_after_point(d)
π = math.pi
π_new = str(π)
print(f'Число π с точностью {d} равно {π_new[0:(number + 2)]}')




