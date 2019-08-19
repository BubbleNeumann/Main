# array sorting --- 21/05/2019
# edited --- 19/08/2019

from random import randint
N = 10
arr = [randint(1, 100) for x in range(N)]
print(arr)
i = a = 1
while a < N:
    a += 1
    for i in range(N - 1):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]

arr.insert(0, arr[N - 1])
del arr[-1]
print(arr)

# 2nd edition:
# import ability


def sort():
    global N
