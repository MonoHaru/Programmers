# LV1 - 추억 점수 문제의 해답
def solution(name: list, yearning: list, photo: list) -> list:
    """photo의 점수를 구합니다.

    각 주어진 name의 점수는 yearning과 같습니다.

    Args:
        name (list[str]): 주어진 이름 리스트.
        yearning (list[int]): 이름과 매칭되는 점수 리스트.
        photo (list[str]): 주어진 photo 리스트.

    Returns:
        list[int]: photo의 점수 리스트.    
    """
    scores = {}
    for i in range(len(name)):
        scores[name[i]] = yearning[i]
    
    answer = []
    for i in range(len(photo)):
        score = 0
        for p in photo[i]:
            if p in scores.keys():
                score += scores[p]
        answer.append(score)
        
    return answer

print(solution(["may", "kein", "kain", "radi"], 
               [5, 10, 1, 3],
               [["may", "kein", "kain", "radi"],
                ["may", "kein", "brin", "deny"], 
                ["kon", "kain", "may", "coni"]]))  # [19, 15, 6]
print(solution(["kali", "mari", "don"],
               [11, 1, 55],
               [["kali", "mari", "don"], 
                ["pony", "tom", "teddy"], 
                ["con", "mona", "don"]]))  # [67, 0, 55]
print(solution(["may", "kein", "kain", "radi"],
               [5, 10, 1, 3], 
               [["may"],
                ["kein", "deny", "may"], 
                ["kon", "coni"]]))  # [5, 15, 0]