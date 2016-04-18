#!/usr/bin/python

fib1 = 1
fib2 = 1
summ = 0
res = 0
MAX = 4000000
fib_seq = [fib1, fib2]

while res < MAX:
  if not res % 2:
    summ += res

  res = fib1 + fib2
  fib1 = fib2
  fib2 = res
  fib_seq.append(res)

print(fib_seq)
print("Sum of even members is %d" % summ)
