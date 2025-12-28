# LV0 - 문자열 붙여서 출력하기 문제의 해답
str1, str2 = input().strip().split(' ')

while True:
    if (len(str1) and len(str2)) >= 1 and (len(str1) and len(str2)) <= 10:
        print(str1+str2)
        break
    else:
        continue