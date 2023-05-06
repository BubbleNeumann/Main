# 1
# inp = input().split(' ')
# print('YES' if sorted(inp) == inp else 'NO')

# 2
# n, m, k = [int(x) for x in input().split(' ')]
# print((n * k // m) + int(n * k % m > 0))

# 3
#     length = int(input())
def get_min_len():
    str = input()
    if len(set(str)) < 4:
        print(-1)
        return

    for substr_len in range(4, length + 1):
        for i in range(length - substr_len):
            if len(set(str[i:i+substr_len])) == 4:
                print(substr_len)
                return
    print(length)


get_min_len()

# 4
def get_min_prefix():
    length = int(input())
    str = input().split(' ')
    for pref_len in range(length, 1, -1):
        str_copy = str
        already_met = False
        occ = str_copy.count(str_copy[0])
        while len(str_copy):
            cnt = str_copy.count(str_copy[0])
            if already_met and cnt != occ:
                break
            if cnt == occ + 1 or (cnt == occ - 1 and cnt == 1):
                already_met = True
            str_copy = [i for i in str_copy if i != str_copy[0]]
            if len(str_copy) == length - pref_len:
                print(pref_len)
                return
    print(2)


get_min_prefix()

# 5
length = int(input())
a = [int(x) for x in input().split(' ')]
res_left = res_right = 0

for i in range(length):
    for j in range(i+1, length+1):
        if sum(a[i:j]) == 0:
            if a[i:j].count(0) == 0:
                res_left += 1 + length - j
            else:
                res_left += 1

if a.count(0) > 0:
    for i in range(length, 0, -1):
        for j in range(i-1, -1, -1):
            if sum(a[j:i]) == 0:
                if a[j:i].count(0) == 0:
                    res_right += 1 + j
                else:
                    res_right += 1
else:
    res_right = res_left

print(min(res_left, res_right))

# 6
n, s = [int(x) for x in input().split(' ')]
res = []
spare_points = s
for i in range(n):
    il, ir = [int(x) for x in input().split(' ')]
    res.append((il, ir))
    spare_points -= il

res.sort(key=lambda x: x[1] - x[0])

if spare_points // (n - n // 2) > res[n//2][1]-res[n//2][0]:
    print(res[n//2][1])
else:
    print(spare_points // (n - n // 2) + res[n//2][0])


