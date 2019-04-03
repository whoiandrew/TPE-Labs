import random

a = [2, 3, 5, 1]
x1 = [random.randrange(1, 21, 1) for i in range(8)]
x2 = [random.randrange(1, 21, 1) for i in range(8)]
x3 = [random.randrange(1, 21, 1) for i in range(8)]
y = [a[0] + a[1] * x1[i] + a[2] * x2[i] + a[3] * x3[i] for i in range(8)]


def cycle_printer(arr):
    for i in arr: print(i, end=" ")

print("\nx1")
cycle_printer(x1)
print("\nx2")
cycle_printer(x2)
print("\nx3")
cycle_printer(x3)
print("\ny")
cycle_printer(y)

avg_y = sum(y) / len(y)
res_y = max([i for i in y if i<avg_y])

x_zero = lambda x: (max(x) + min(x)) / 2
dx = lambda x: x_zero(x) - min(x)
xn = lambda x: (i - x_zero(x)) / dx(x)
y_etalon = a[0] + a[1] * x_zero(x1) + a[2] * x_zero(x2) + a[3] * x_zero(x3)

print(f"\n\nAVG of y arr - {avg_y}\n\u2192Y\u0305 - {res_y} - The answer!!!")
print(f"\nX(0)1 - {x_zero(x1)}\ndx1 - {dx(x1)}\nX(0)2 - {x_zero(x2)}\ndx2 - {dx(x2)}\nX(0)3 - {x_zero(x3)}\ndx3 - {dx(x3)}\n")
print(f"y(et) - {y_etalon}\n")

xn1 = []
xn2 = []
xn3 = []

for i in x1: xn1.append(xn(x1))
for i in x2: xn2.append(xn(x2))
for i in x3: xn3.append(xn(x3))
print("xn1")
for i in xn1: print(f"{i:.5f}", end=" ")
print("\nxn2")
for i in xn2: print(f"{i:.5f}", end=" ")
print("\nxn3")
for i in xn3: print(f"{i:.5f}", end=" ")
print("\n")