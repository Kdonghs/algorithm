def check(str_list):
    stack = []

    for _str in str_list:
        if _str in ('[', '(', '{'):
            stack.append(_str)
        else:
            if not stack: return False
            x = stack.pop()
            if _str == ']' and x != '[':
                return False
            elif _str == ')' and x != '(':
                return False
            elif _str == '}' and x != '{':
                return False

    if stack: return False
    return True

def solution(s):
    answer = 0
    for i in range(len(s)):
        u = s[:i]
        v = s[i:]

        if check(v+u):
            answer +=1
    return answer