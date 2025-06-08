from collections import deque

c = 11
b = 2


def catch_me(cony_loc, brown_loc):
    MAX = 200000
    visited = [[False] * (MAX + 1) for _ in range(2)]

    queue = deque()
    queue.append(brown_loc)
    visited[0][brown_loc] = True

    time = 0
    while True:
        cony_pos = cony_loc + time * (time + 1) // 2
        if cony_pos > MAX:
            return -1  # 코니가 범위 밖으로 도망감
        if visited[time % 2][cony_pos]:
            return time  # 브라운이 해당 시간에 잡음

        for _ in range(len(queue)):
            curr = queue.popleft()
            for next_pos in (curr - 1, curr + 1, curr * 2):
                if 0 <= next_pos <= MAX and not visited[(time + 1) % 2][next_pos]:
                    visited[(time + 1) % 2][next_pos] = True
                    queue.append(next_pos)

        time += 1
    return


print(catch_me(c, b))  # 5가 나와야 합니다!

print("정답 = 3 / 현재 풀이 값 = ", catch_me(10,3))
print("정답 = 8 / 현재 풀이 값 = ", catch_me(51,50))
print("정답 = 28 / 현재 풀이 값 = ", catch_me(550,500))