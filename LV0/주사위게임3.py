# LV0 - 주사위 게임 3 문제의 해답
def find_key(dictionary, indice):
    for key, value in dictionary.items():
        if value == indice:
            return key

def find_two_keys(dictionary, indice):
    res = []
    for key, value in dictionary.items():
        if value == indice:
            res.append(key)
    return res
        
def solution(a, b, c, d):
    length = len(set([a, b, c, d]))
    score_dice = {}
    
    for i in [a, b, c, d]:
        if i not in score_dice.keys():
            score_dice[i] = 1
        else:
            score_dice[i] += 1
    
    if length == 4:
        return min([a, b, c, d])
    elif length == 3:
        q, r = find_two_keys(score_dice, 1)
        return q * r
    elif length == 2:
        if max(score_dice.values()) == 2:
            p, q = score_dice.keys()
            return (p + q) * abs((p - q))
        elif max(score_dice.values()) == 3:
            p = find_key(score_dice, 3)
            q = find_key(score_dice, 1)
        return (10 * p + q) ** 2
    elif length == 1:
        return 1111 * a