input = 20


def find_prime_list_under_number(number):
    arr = []

    for i in range(2, number + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                continue
        if is_prime:
            arr.append(i)
    return arr

result = find_prime_list_under_number(20)
print(result)

def find_prime_list_under_number2(number):      #개선한코드, 소수는 자신의 제곱근 보다 큰수로 나누어지지않는다.
    arr = []
    for i in range(2, number + 1):
        for j in arr:
            if j*j <= i and i % j == 0:
                break
        else:
            arr.append(i)
    return arr

result = find_prime_list_under_number2(20)
print(result)