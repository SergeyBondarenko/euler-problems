#!/usr/bin/python
n = 600851475143
i = 2

while i * i < n:
    while not n % i:
        n /= i
    i += 1

print n
