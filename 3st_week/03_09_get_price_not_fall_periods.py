prices = [1, 2, 3, 2, 3]

# 큐 내가 푼 풀이(이중 반복문), 시간복잡도 = N * M
def get_price_not_fall_periods(prices):
    array = [0] * len(prices)
    for i in range(len(prices)):
        first = prices[i]
        for j in range(i + 1, len(prices)):
            second = prices[j]
            if first <= second:
                array[i] +=1
            else:
                array[i] +=1
                break
    return array


print(get_price_not_fall_periods(prices))

print("정답 = [4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods(prices))
print("정답 = [6, 2, 1, 3, 2, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [6, 1, 4, 3, 1, 1, 0] / 현재 풀이 값 = ", get_price_not_fall_periods([1, 5, 3, 6, 7, 6, 5]))