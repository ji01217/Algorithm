def func(string):
    # 올바른 괄호인지 판단
    global answer
    stack = []
    for s in string:
        if s == "(" or s == "{" or s == "[":
            stack.append(s)
        else:
            if len(stack) == 0:
                return
            if s == ")":
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return
            if s == "}":
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return
            if s == "]":
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return
    if len(stack) == 0:
        answer += 1
    return

def solution(s):
    global answer
    answer = 0
    ss = s + s
    ls = len(s)
    for i in range(ls):
        func(ss[i:i+ls])
        
    return answer