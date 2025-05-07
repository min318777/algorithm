def is_correct_parenthesis(string):

    stack = []
    for i in string:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False

    if stack:
        return False
    return True


print("정답 = True / 현재 풀이 값 = ", is_correct_parenthesis("(())"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis(")"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())))"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("())()"))
print("정답 = False / 현재 풀이 값 = ", is_correct_parenthesis("((())"))