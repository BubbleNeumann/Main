main = [0] * 17

number = int(input())
for i in range(number):
    x = int(input())
    main[x] +=1

sum = 0
for i in range(len(main)):
    sum += main[i]

while sum > 0:
    max = main[0]
    out = 0
    for i in range(len(main)):
        if main[i] > max:
            max = main[i]
            out = i
    print(out, ' ', max)
    main[out] = 0
    
    sum = 0
    for i in range(len(main)):
        sum += main[i]


