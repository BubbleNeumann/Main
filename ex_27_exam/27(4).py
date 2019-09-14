N = int(input())
a = [None] * 145
for i in range(N):
    x = int(input())
    if a[x%144] == None:
        a[x%144] = x
    elif  x < a[x%144]:
        a[x%144] = x
min = 1200 * 144 + 1
for i in range(122):
    if a[i] != None and a[144-i] != None:
        x = a[i] + a[144-i]
        if x < min and a[i] < a[144-i]:
            min = x
if min == 1200 * 144 + 1: min == 0
print(min)
        
        
    
