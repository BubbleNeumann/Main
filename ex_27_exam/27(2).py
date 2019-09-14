N = int(input())
arr = []
for i in range(N):
    x = int(input())
    arr.append(x)
min = 12001
for i in range(len(arr)-1):
    j = i + 1
    for j in range(len(arr)-i):
        x = arr[i] + arr[j]
        if x%144 == 0 and arr[i] < arr[j] and i < j:
            if x < min:
                min = x
if min == 12001: print(0)
else: print(min)
    
        

