import heapq
from importlib.util import source_hash

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30


# 1. supply_dates의 인덱스(공급일)가 stock보다 적어야한다. 왜? 밀가루재고가 4이면 4일뒤에 재고가 없으므로 stock < supply_dates
# 2. stock이 supply_recover_k보다 높아질때까지 반복해야한다.
def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    answer = 0
    max_heap = []
    index = 0
    while stock < k:
        while index < len(dates) and dates[index] <= stock:

            heapq.heappush(max_heap, supplies[index] * -1)
            index += 1

        stock += heapq.heappop(max_heap) * -1
        answer += 1

    return answer


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
print("정답 = 2 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15], [20, 5, 10], 30))
print("정답 = 4 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(4, [4, 10, 15, 20], [20, 5, 10, 5], 40))
print("정답 = 1 / 현재 풀이 값 = ", get_minimum_count_of_overseas_supply(2, [1, 10], [10, 100], 11))