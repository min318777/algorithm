input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    one_to_zero = 0
    zero_to_one = 0
    for i in range(len(string)-1):
        if string[i] == "1":
            if string[i+1] == "0":
                one_to_zero += 1
        else:
            if string[i+1] == "1":
                zero_to_one += 1
    print(one_to_zero, zero_to_one)
    return min([one_to_zero, zero_to_one])

result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)