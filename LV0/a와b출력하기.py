# LV0 - a와 b 출력하기 문제의 해답
a, b = map(int, input().strip().split(' '))

while True:
    if (a and b) >= -100000 and (a and b) <= 100000:
        print('a =', a)
        print('b =', b)
        break
    else:
        continue