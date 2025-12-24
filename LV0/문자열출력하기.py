str = input()

while True:
    if len(str) >= 1 and len(str) <= 1000000 and str != '':
        print(str)
        break
    else:
        continue