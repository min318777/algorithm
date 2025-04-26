input = "abadabac"

def find_not_repeating_first_character(string):

    arr = [0] * 26
    arr_not = []
    for char in string:
        arr[ord(char) - 97] += 1

    for i in range(26):
        if arr[i] == 1:
            arr_not.append(chr(i + 97 ))

    for i in string:
        if i in arr_not:
            return i
    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("aabbcddd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))