# LV2 - 튜플 문제의 해답
def solution(s):
    """
    :param s: str
    :return: list
    """
    answer = []
    
    parts = [x.strip('{}') for x in s.split('},{')]
    new_s = [list(map(int, x.split(','))) for x in parts]
    new_s.sort(key = len)
    
    for t in new_s:
        for i in range(len(t)):
            if t[i] not in answer:
                answer.append(t[i])
                
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))  # [2, 1, 3, 4]
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))  # [2, 1, 3, 4]
print(solution("{{20,111},{111}}"))  # [111, 20]
print(solution("{{123}}"))  # [123]
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))  # [3, 2, 4, 1]