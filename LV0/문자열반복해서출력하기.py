# LV0 - 문자열 반복해서 출력하기 문제의 해답
str, n = input().strip().split(' ')
n = int(n)

while True:
    if len(str) < 1 and len(str) > 10 and n < 1 and n > 5:
        continue
    else:
        print(str*n)
        break