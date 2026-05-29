# LV0 - 모스부호 (1) 문제의 해답
def solution(letter: str) -> str:
    """암호 letter를 모스부호를 사용해 해독합니다.

    Args:
        letter (str): 암호 문자열.

    Returns:
        str: 해독 문자.    
    """
    morse = {
        '.-':   'a', '-...': 'b', '-.-.': 'c',
        '-..':  'd', '.':    'e', '..-.': 'f',
        '--.':  'g', '....': 'h', '..':   'i',
        '.---': 'j', '-.-':  'k', '.-..': 'l',
        '--':   'm', '-.':   'n', '---':  'o',
        '.--.': 'p', '--.-': 'q', '.-.':  'r',
        '...':  's', '-':    't', '..-':  'u',
        '...-': 'v', '.--':  'w', '-..-': 'x',
        '-.--': 'y', '--..': 'z'
    }
    
    answer = ''
    
    letter = letter.split(' ')
    for sign in letter:
        answer += morse[sign]    
    
    return answer

print(solution(".... . .-.. .-.. ---"))     # "hello"
print(solution(".--. -.-- - .... --- -."))  # "python"