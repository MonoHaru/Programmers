# LV0 - 대소문자 바꿔서 출력하기 문제의 해답
str = input()

while True:
    if len(str) < 1 and len(str) > 20:
        continue
    else:
        print(str.swapcase())
        break