import datetime as dt
import sys

def fibonacci(n):
	a, b = 0, 1
	for _ in range(n):
		yield(a)
		a, b = b, a + b

count = int(input("Enter the size of the fibonacci list: "))
fibo_list = [None] * count

t1 = dt.datetime.now()
g = fibonacci(count)

g_mem = sys.getsizeof(g)

for i in range(count):
	fibo_list[i] = (next(g))

print(fibo_list)
t2 = dt.datetime.now()
dt_gen = t2 - t1
print(f"Completed in: {dt_gen}")
print(f"Memory: {g_mem}")
