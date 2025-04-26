
def find_max_plus_or_multiply(array):               # 내가 푼 풀이 -> 답은 맞지만 방식은 강의와 다름
    answer = 0                                      # 시간복잡도 -> N + 5 -> O(N)
    plus = array[0]
    multiply = array[0]
    for num in array[1:]:
        plus = plus + num
        multiply = multiply * num
        if plus > multiply:
            answer = plus
        else:
            answer = multiply

        plus = answer
        multiply = answer

    return answer

result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))


def find_max_plus_or_multiply(array):               # 강의 풀이
    plus_or_multiply = 0
    for num in array:
        if plus_or_multiply <= 1 or num <= 1:
            plus_or_multiply += num
        else:
            plus_or_multiply *= num
    return plus_or_multiply


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))

