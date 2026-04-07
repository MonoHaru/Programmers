# LV0 - 조건에 맞게 수열 변환하기 2 문제의 해답
def solution(arr):
    """
    :param arr: list
    :return: int
    """
    bool_arr = [1] * len(arr)
    ans = 0
    while True:
        if sum(bool_arr) == 0:
            break

        ans += 1
        
        for i in range(len(arr)):
            if bool_arr[i]:
                tmp = renewal(arr[i])
                if tmp == arr[i]:
                    bool_arr[i] = 0
                arr[i] = tmp
        
    return ans - 1

def renewal(n):
    if n >= 50 and n % 2 == 0:
        return n // 2
    elif n < 50 and n % 2 == 1:
        return n * 2 + 1
    else:
        return n
    
print(solution([1, 2, 3, 100, 99, 98]))  # 5