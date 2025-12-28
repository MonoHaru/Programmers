# LV0 - 문자열 돌리기 문제의 해답
str = input()

while True:
    if len(str) >= 1 and len(str) <= 10:
        for s in str:
            print(s)
        break
    else:
        continue