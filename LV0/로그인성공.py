# LV0 - 로그인 성공? 문제의 해답
def solution(id_pw: list, db: list) -> str:
    """로그인 여부를 알려줍니다.

    Args:
        id_pw (list[str]): 주어진 ID와 PW.
        db (list[str]): 기존 로그인 데이터베이스.

    Returns:
        str: 로그인 성공한다면 "login", PW가 틀리면 "wrong pw", 실패하면 "fail".    
    """
    for us, pw in db:
        if us == id_pw[0] and pw == id_pw[1]:
            return "login"
        elif us == id_pw[0]:
            return "wrong pw"
    return "fail"

print(solution(["meosseugi", "1234"],
               [["rardss", "123"], 
                ["yyoom", "1234"], 
                ["meosseugi", "1234"]]
                ))  # "login"
print(solution(["programmer01", "15789"],
               [["programmer02", "111111"], 
                ["programmer00", "134"], 
                ["programmer01", "1145"]]
                ))  # "wrong pw"
print(solution(["rabbit04", "98761"], 
               [["jaja11", "98761"], 
                ["krong0313", "29440"], 
                ["rabbit00", "111333"]]
                ))  # "fail"