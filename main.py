import datetime as dt
import sys

def fibonacci(n):
	a, b = 0, 1
	for _ in range(n):
		yield(a)
		a, b = b, a + b

qte = 100
fibo_list = [None] * qte

t1 = dt.datetime.now()
g = fibonacci(qte)
t2 = dt.datetime.now()

dt_gen = t2 - t1

g_mem = sys.getsizeof(g)

for i in range(qte):
	fibo_list[i] = (next(g))

print(fibo_list)
print(f"Completed in: {dt_gen}")
print(f"Memory: {g_mem}")
