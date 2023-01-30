def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append("(")
        else:
            if stack:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            else:
                return False
    if stack:
        return False
    return True