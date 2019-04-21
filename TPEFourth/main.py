import random
import numpy.linalg as l
import copy
from tables import *
import math


def cycle_printer(arr):
    for i in arr: print(i)


x1 = [-5, 15]
x2 = [25, 45]
x3 = [15, 45]

m = 3
N = 8
q = 0.05

x = [[min(x1), min(x1), min(x1), min(x1), max(x1), max(x1), max(x1), max(x1)],
     [min(x2), min(x2), max(x2), max(x2), min(x2), min(x2), max(x2), max(x2)],
     [min(x3), max(x3), min(x3), max(x3), max(x3), min(x3), max(x3), min(x3)]]

x_avg = [(max(x1) + max(x2) + max(x3)) / 3, (min(x1) + min(x2) + min(x3)) / 3]

y_range = [200 + max(x_avg), 200 + min(x_avg)]
while True:
    y = [[round(random.uniform(min(y_range), max(y_range)), 4) for i in range(m)] for j in range(N)]
    avg_of_arr = lambda arr: round(sum(arr) / len(arr), 4)
    y_avg = list(map(avg_of_arr, y))
    print("\nMatrix of experiment's planning: \n")
    for i in range(N):
        print(f"{[x[j][i] for j in range(3)]}  {[y[i][j] for j in range(m)]}  {y_avg[i]}")

    mx = list(map(avg_of_arr, x))


    def foo(*args):
        res = [1 for _ in range(len(args[0]))]
        for i in range(len(args[0])):
            for j in args:
                res[i] *= j[i]
        return res


    forb = ([1 for _ in range(8)], x[0], x[1], x[2], foo(x[0], x[1]), foo(x[0], x[2]), foo(x[1], x[2]),
            foo(x[0], x[1], x[2]))
    ms = list(list(sum(foo(forb[i], forb[j])) for j in range(8)) for i in range(8))
    k = [sum(foo(y_avg, forb[i])) for i in range(N)]

    my_det = l.det(ms)


    def det_getter(num):
        det_i = copy.deepcopy(ms)
        for i in range(N):
            det_i[i][num] = k[i]
        return det_i


    b = [l.det(det_getter(i)) / my_det for i in range(N)]

    y_regr = [round(
        b[0] + b[1] * x[0][i] + b[2] * x[1][i] + b[3] * x[2][i] + b[4] * x[0][i] * x[1][i] + b[5] * x[0][i] * x[2][i] + \
        b[6] * x[1][i] * x[2][i] + b[7] * x[0][i] * x[1][i] * x[2][i], 4) for i in range(N)]
    print("\n\n")
    cycle_printer(y_regr)

    f1 = m - 1
    f2 = N
    f3 = f1 * f2
    D = []
    for i in range(N):
        tmp = 0
        for num in range(m):
            tmp+= (y[i][num] - y_regr[i])**2
        D.append(tmp)

    print(D)

    Gp = max(D) / sum(D)
    Gt = G_table[f2 - 2][f1 - 1] * 0.0001

    print("Однорідність дисперсії (критерій Кохрена): ")
    print(f"Gp = {Gp}")
    print(f"Gt = {Gt}")
    if Gp < Gt:
        print("Дисперсія однорідна (Gp < Gt)")
        break
    else:
        print("Дисперсія неоднорідна (Gp > Gt), збільшуємо m, повторюємо операції")
        m+=1

Sb = sum(D) / N
Sbs = Sb / (N * m)

beta = [(y_regr[0] + y_regr[1] + y_regr[2] + y_regr[3] + y_regr[4] + y_regr[5] + y_regr[6] + y_regr[7])/N,
    (-y_regr[0] - y_regr[1] - y_regr[2] - y_regr[3] + y_regr[4] + y_regr[5] + y_regr[6] + y_regr[7])/N,
    (-y_regr[0] - y_regr[1] + y_regr[2] + y_regr[3] - y_regr[4] - y_regr[5] + y_regr[6] + y_regr[7])/N,
    (-y_regr[0] + y_regr[1] - y_regr[2] + y_regr[3] - y_regr[4] + y_regr[5] - y_regr[6] + y_regr[7])/N,
    (y_regr[0] + y_regr[1] - y_regr[2] - y_regr[3] - y_regr[4] - y_regr[5] + y_regr[6] + y_regr[7])/N,
    (y_regr[0] - y_regr[1] + y_regr[2] - y_regr[3] - y_regr[4] + y_regr[5] - y_regr[6] + y_regr[7])/N,
    (y_regr[0] - y_regr[1] - y_regr[2] + y_regr[3] + y_regr[4] - y_regr[5] - y_regr[6] + y_regr[7])/N,
    (-y_regr[0] + y_regr[1] + y_regr[2] - y_regr[3] + y_regr[4] - y_regr[5] - y_regr[6] + y_regr[7])/N]

t = [abs(i)/Sbs for i in beta]

t_kr = t_table[f3-1]

print(t_kr)
print(t)

t_final = list(filter(lambda x: x>t_kr, t))
f4 = N-len(t_final)
print(f"\nЗначимі коефіцієнти: ")
cycle_printer(t_final)
print("\n")
print(t)
print(t_final)
print(beta)


fisher_sum = 0
for i in range(N):
      fisher_sum += pow((t[i] - y_regr[i]), 2)
D_ad = (m/(f4))*fisher_sum
Fp = D_ad/Sb
print(f"Fp = {Fp}")
Ft = F_table[f3-1][f4-1]
print(f"Ft = {Ft}")
if Ft > Fp:
      print(f"Ft > Fp\nРівняння регресії адекватно оригіналу при рівні значимості {q}")
else:
      print(f"Ft < Fp\nРівняння регресії неадекватно оригіналу при рівні значимості {q}")
