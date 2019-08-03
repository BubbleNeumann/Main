# array sorting --- 21/05/2019

from random import randint
N = 10
l = [randint(1, 100) for x in range(N)]
print(l)
i = a = 1
while a < N:
    a += 1
    for i in range(N - 1):
        if l[i - 1] > l[i]:
            l[i - 1], l[i] = l[i], l[i - 1]

l.insert(0, l[N - 1])
del l[-1]
print(l)
