queries = [[0, 4, 2],[0, 3, 2],[0, 2, 2]]
arr = [0, 1, 2, 4, 3]
# arr[0:4].sort()
# print(sorted(arr))
answer = []
for s, e, k in queries:
    tmp = []
    for x in sorted(arr[s:e+1]):
        if x > k:
            tmp.append(x)
            break
    answer.append(-1 if not tmp else tmp[0])
     #   if i == len(list) - 1:
      #      answer.append(-1)
print(answer)