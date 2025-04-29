def find_max_occurred_alphabet(string):

    arr = [0] * 26
    for c in string:
        if c.isalpha():
            arr[ord(c)-ord('a')] += 1
        else:
            continue
    max_num = max(arr)
    result2 = 'a'
    for num in arr:
        if num == max_num:
            result2 = chr(num)

    return result2


result = find_max_occurred_alphabet

print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))