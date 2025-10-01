
a = 1234
res = 0

while a != 0:
    res = (res * 10) +  a % 10
    a = a // 10

