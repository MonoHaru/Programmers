# LV0 = 덧셈식 출력하기 문제의 해답
a, b = map(int, input().strip().split(' '))

while True:
    if (a and b) < 1 and (a and b) > 100:
        continue
    else:
        print(f'{a} + {b} = {a+b}')
        break