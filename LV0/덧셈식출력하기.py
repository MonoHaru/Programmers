a, b = map(int, input().strip().split(' '))

while True:
    if (a and b) < 1 and (a and b) > 100:
        continue
    else:
        print(f'{a} + {b} = {a+b}')
        break