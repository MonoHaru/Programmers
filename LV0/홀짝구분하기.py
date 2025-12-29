# LV0 - 홀짝 구분하기 문제의 해답
n = int(input())

while True:
    if n >= 1 and n <= 1000:
        print(f'{n} is odd' if n % 2 else f'{n} is even')
        break
    else:
        continue