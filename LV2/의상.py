def solution(clothes):
    dict_clothes = dict()
    for name, type in clothes:
        if type not in dict_clothes.keys():
            dict_clothes[type] = 2
        else:
            dict_clothes[type] += 1
            
    cnt = 1
    for key, value in dict_clothes.items():
        cnt *= value
    return cnt - 1

print(solution([["yellow_hat", "headgear"], 
                ["blue_sunglasses", "eyewear"], 
                ["green_turban", "headgear"]]))  # 5
print(solution([["crow_mask", "face"], 
                ["blue_sunglasses", "face"], 
                ["smoky_makeup", "face"]]))  # 3