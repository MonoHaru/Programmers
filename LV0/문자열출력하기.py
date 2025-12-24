# LV0 - 문자열출력하기 문제의 해답
str = input()

while True:
    if len(str) >= 1 and len(str) <= 1000000 and str != '':
        print(str)
        break
    else:
        continue