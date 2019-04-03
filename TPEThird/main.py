"""TPE Third lab
   Made by Andrii Doroshenko @whoiandrew"""
import random
import numpy.linalg as l
import math
from tables import *

#variant 308
x1 = [-30, 0]
x2 = [-15, 35]
x3 = [-30, 35]

m = 3
N = 4
q = 0.05

x_matr = [[min(x1), min(x1), max(x1), max(x1)],
          [min(x2), max(x2), min(x2), max(x2)],
          [min(x3), max(x3), max(x3), min(x3)]]

x_avg_max = (max(x1) + max(x2) + max(x3)) / 3
x_avg_min = (min(x1) + min(x2) + min(x3)) / 3

y_max = 200 + x_avg_max
y_min = 200 + x_avg_min

#m
while True:
      y = [[round(random.uniform(y_min, y_max), 4) for i in range(m)] for j in range(4)]

      print("y1, y2, y3, ..., ym:")
      for i in y: print(i)
      print("\n")
      for i in range(len(x_matr)): print(f"{x_matr[i]} - x{i+1}")

      avg_arr = lambda arr: sum(arr) / len(arr)

      y_avg_arr = list(map(avg_arr, y))
      print(f"\naverage y(i): {y_avg_arr}")

      mx_arr = list(map(avg_arr, x_matr))
      print(f"\n mx(i): {mx_arr}")

      my = avg_arr(y_avg_arr)
      print(f"\nmy = {my}")

      a = lambda x: (x[0] * y_avg_arr[0] + x[1] * y_avg_arr[1] + x[2] * y_avg_arr[2] + x[3] * y_avg_arr[3]) / 4

      a1 = a(x_matr[0])
      a2 = a(x_matr[1])
      a3 = a(x_matr[2])

      a11 = (x_matr[0][0] * x_matr[0][0] + x_matr[0][1] * x_matr[0][1] + x_matr[0][2] * x_matr[0][2] + x_matr[0][3] *
             x_matr[0][3]) / 4
      a22 = (x_matr[1][0] * x_matr[1][0] + x_matr[1][1] * x_matr[1][1] + x_matr[1][2] * x_matr[1][2] + x_matr[1][3] *
             x_matr[1][3]) / 4
      a33 = (x_matr[2][0] * x_matr[2][0] + x_matr[2][1] * x_matr[2][1] + x_matr[2][2] * x_matr[2][2] + x_matr[2][3] *
             x_matr[2][3]) / 4
      a12 = a21 = (x_matr[0][0] * x_matr[1][0] + x_matr[0][1] * x_matr[1][1] + x_matr[0][2] * x_matr[1][2] + x_matr[0][3] *
                   x_matr[1][3]) / 4
      a13 = a31 = (x_matr[0][0] * x_matr[2][0] + x_matr[0][1] * x_matr[2][1] + x_matr[0][2] * x_matr[2][2] + x_matr[0][3] *
                   x_matr[2][3]) / 4
      a23 = a32 = (x_matr[1][0] * x_matr[2][0] + x_matr[1][1] * x_matr[2][1] + x_matr[1][2] * x_matr[2][2] + x_matr[1][3] *
                   x_matr[2][3]) / 4

      print(f"""\na1 = {a1}, a2 = {a2}, a3= {a3},
      a11 = {a11}, a12 = {a12}, a13 = {a13},
      a21 = {a21}, a22 = {a22}, a23= {a23},
      a31 = {a31}, a32 = {a32}, a33= {a33}\n""")

      det = lambda sq_matr: round(l.det(sq_matr), 4)

      mm = [[1, mx_arr[0], mx_arr[1], mx_arr[2]],
            [mx_arr[0], a11, a12, a13],
            [mx_arr[1], a12, a22, a32],
            [mx_arr[2], a13, a23, a33]]

      m0 = [[my, mx_arr[0], mx_arr[1], mx_arr[2]],
            [a1, a11, a12, a13],
            [a2, a12, a22, a32],
            [a3, a13, a23, a33]]

      m1 = [[1, my, mx_arr[1], mx_arr[2]],
            [mx_arr[0], a1, a12, a13],
            [mx_arr[1], a2, a22, a32],
            [mx_arr[2], a3, a23, a33]]

      m2 = [[1, mx_arr[0], my, mx_arr[2]],
            [mx_arr[0], a11, a1, a13],
            [mx_arr[1], a12, a2, a32],
            [mx_arr[2], a13, a3, a33]]

      m3 = [[1, mx_arr[0], mx_arr[1], my],
            [mx_arr[0], a11, a12, a1],
            [mx_arr[1], a12, a22, a2],
            [mx_arr[2], a13, a23, a3]]

      b = [det(m0) / det(mm), det(m1) / det(mm), det(m2) / det(mm), det(m3) / det(mm)]

      print(f"\nb(i): {b}")

      y1_avg = b[0] + b[1] * min(x1) + b[2] * min(x2) + b[3] * min(x3)
      y2_avg = b[0] + b[1] * min(x1) + b[2] * max(x2) + b[3] * max(x3)
      y3_avg = b[0] + b[1] * max(x1) + b[2] * min(x2) + b[3] * max(x3)
      y4_avg = b[0] + b[1] * max(x1) + b[2] * max(x2) + b[3] * min(x3)

      D1 = (pow((y[0][0] - y1_avg), 2) + pow((y[0][1] - y1_avg), 2) + pow((y[0][2] - y1_avg), 2)) / 3
      D2 = (pow((y[1][0] - y2_avg), 2) + pow((y[1][1] - y2_avg), 2) + pow((y[1][2] - y2_avg), 2)) / 3
      D3 = (pow((y[2][0] - y3_avg), 2) + pow((y[2][1] - y3_avg), 2) + pow((y[2][2] - y3_avg), 2)) / 3
      D4 = (pow((y[3][0] - y4_avg), 2) + pow((y[3][1] - y4_avg), 2) + pow((y[3][2] - y4_avg), 2)) / 3
      D = [D1, D2, D3, D4]
      print(f"\nD(i): {D}")
      f1 = m - 1
      f2 = N
      print(f"f1 = m - 1 = {f1}")
      print(f"f2 = N = {f2}")
      Gp = max(D) / sum(D)
      Gt = G_table[f2-2][f1-1]*0.0001
      print("Однорідність дисперсії (критерій Кохрена): ")
      print(f"Gp = {Gp}")
      print(f"Gt = {Gt}")
      if Gp < Gt:
            print("Дисперсія однорідна (Gp < Gt)")
            break
      else:
            print("Дисперсія неоднорідна (Gp > Gt), збільшуємо m, повторюємо операції")
            m+=1


print("\n\nКритерій Стьюдента:")
Sb = sum(D) / N

Sbs = math.sqrt(Sb / (N * m))
print(f"S{{beta}} = {Sbs}")

beta = [(y1_avg + y2_avg + y3_avg + y4_avg)/4,
        (-y1_avg - y2_avg + y3_avg + y4_avg)/4,
        (-y1_avg + y2_avg - y3_avg + y4_avg)/4,
        (-y1_avg + y2_avg + y3_avg - y4_avg)/4]

print(f"beta(i): {beta}")

t=[]
for i in beta:
      t.append(abs(i)/Sbs)
print(f"t(i): {t}")

f3 = f1*f2
print(f"f3 = f1 * f2 = {f3}")
t_kr = t_table[f3]
print(f"t_kr = {t_kr}")
print(f"t(i) < t_kr: {[i for i in t if i<=t_kr]}")
print(f"\nНезначимі коефіцієнти: {[b[i] for i in range(len(t)) if t[i]<=t_kr]}")
print(f"Значимі коефіцієнти: {[b[i] for i in range(len(t)) if t[i]>t_kr]}")
t_final = list(filter(lambda x: x<t_kr, t))

for i in range(len(t)):
      if t[i] <= t_kr:
            b[i] = 0

y_t1 = b[0] + b[1] *  x_matr[0][0] + b[2] * x_matr[1][0] + b[3]* x_matr[2][0]
y_t2 = b[0] + b[1] *  x_matr[0][1] + b[2] * x_matr[1][1] + b[3]* x_matr[2][1]
y_t3 = b[0] + b[1] *  x_matr[0][2] + b[2] * x_matr[1][2] + b[3]* x_matr[2][2]
y_t4 = b[0] + b[1] *  x_matr[0][3] + b[2] * x_matr[1][3] + b[3]* x_matr[2][3]
y_t = [y_t1, y_t2, y_t3, y_t4]
print(f"y average(i): {y_t}")
print("\nКритерій Фішера:")
d = N - len(t_final)
f4 = N-d
print(f"f4 = N - d = {f4}")

fisher_sum = 0
for i in range(0, N):
      fisher_sum += pow((y_t[i] - y_avg_arr[i]), 2)
D_ad = (m/(N-d))*fisher_sum
Fp = D_ad/Sb
print(f"Fp = {Fp}")
Ft = F_table[f3-1][f4-1]
print(f"Ft = {Ft}")
if Ft > Fp:
      print(f"Ft > Fp\nРівняння регресії адекватно оригіналу при рівні значимості {q}")
else:
      print(f"Ft < Fp\nРівняння регресії неадекватно оригіналу при рівні значимості {q}")








