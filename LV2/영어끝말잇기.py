# LV2 - 영어 끝말잇기 문제의 해답
def solution(n, words):
    """
    :param n: int
    :param words: list
    :return: list
    """
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [i % n + 1, i // n + 1]
    return [0, 0]

n = 3
words = ["tank", "kick", "know", "wheel", "land", 
         "dream", "mother", "robot", "tank"]
print(solution(n, words))  # [3, 3]

n = 5
words = ["hello", "observe", "effect", "take", "either", 
         "recognize", "encourage", "ensure", "establish", 
         "hang", "gather", "refer", "reference", "estimate", 
         "executive"]
print(solution(n, words))  # [0, 0]

n = 2
words = ["hello", "one", "even", "never", 
         "now", "world", "draw"]
print(solution(n, words))  # [1, 3]