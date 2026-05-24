# LV0 - 커피 심부름 문제의 해답
def solution(order: list) -> int:
    """음료의 총 가격을 찾습니다.

    라떼는 5000이고, 그외는 4500입니다.

    Args:
        order (list[int]): 주문 리스트.

    Returns:
        int: 주문의 총 가격.    
    """
    answer = 0
    for o in order:
        if "latte" in o:
            answer += 5000
        else:
            answer += 4500
    return answer

print(solution([
    "cafelatte", 
    "americanoice", 
    "hotcafelatte", 
    "anything"
]))  # 19000
print(solution([
    "americanoice", 
    "americano", 
    "iceamericano"
]))  # 13500