def solution(s):
    test = []
    for i in s:
        if i == "(":
            test.append(i)
        else:
            if check(test) and i == ")":
                return False
            elif not check(test) and i == ")":
                test.pop()
    if check(test) == True:
        return True
    else:
        return False
        
        
def check(data):
    if not data:
        return True
    