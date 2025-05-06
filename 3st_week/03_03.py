top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):

    stack = [0]
    stack2 = []
    stack2.append(heights[0])
    idx = 0
    for i in range(1, len(heights) - 1):
        if heights[i] > stack2[-1]:
            while len(stack2) != 0 and heights[i] <= stack2[-1]:
                stack2.pop()
            stack.append(idx)
            idx = i + 1
            stack2.append(heights[i])
        else:
            stack.append(idx)
            stack2.append(heights[i])


    return stack


print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))