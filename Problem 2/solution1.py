#!/usr/bin/python

fib3 = 2
fib6 = 0
summ = 0
result = 2
MAX = 4000000
fib_seq_even = [fib3]

while result < MAX:
  summ += result

  result = 4 * fib3 + fib6
  fib6 = fib3
  fib3 = result
  fib_seq_even.append(result)

print(fib_seq_even)
print(summ)
