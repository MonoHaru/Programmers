# LV0 - 문자열 겹쳐쓰기 문제의 해답
def solution(my_string, overwrite_string, s):
    try:
        return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]
    except Exception as ex:
        print('[INFO] Error:', ex)
        return None