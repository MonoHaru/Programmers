def solution(numlist, n):
    answer = []
    
    pivot = 0
    for i, num in enumerate(sorted(numlist)):
        if num - n <= 0:
            pivot = i
        answer.append(num - n)
    print(pivot, answer)
    
    sorting = []
    temp = pivot + 1
    while True:
        if pivot < 0 and temp == len(answer):
            break
        elif pivot < 0:
            sorting.append(answer[temp])
        elif 
    return answer

print(solution([1, 2, 3, 4, 5, 6], 4))