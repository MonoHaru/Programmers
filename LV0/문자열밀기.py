# LV0 - 문자열 밀기 문제의 해답
def solution(A: str, B: str) -> int:
    """A를 밀어 B가 되는 횟수를 셉니다.

    Args:
        A (str): 밀릴 문자열.
        B (str): 확인 문자열.

    Returns:
        int: 가능하면 횟수, 안되면 -1을 반환합니다.    
    """
    answer = 0
    while A != B:
        A = A[-1] + A[:-1]
        if answer == len(A):
            return -1
        answer += 1
    return answer

print(solution("hello", "ohell"))  # 1
print(solution("apple", "elppa"))  # -1
print(solution("atat", "tata"))    # 1
print(solution("abc", "abc"))      # 0