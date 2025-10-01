import math

n = int(input("cho 1 số"))
m = int(input("cho 1 số"))
k  = n / 2
res = 0
if k % m  == 0:
    print(k)
if k % m != 0:
    print(k - 1 + m)