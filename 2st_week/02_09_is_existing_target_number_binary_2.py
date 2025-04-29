
def is_exist_target_number_binary(target, array):

    array.sort()
    current_min = 0
    current_max = len(array) - 1
    current_mid = (current_min + current_max) // 2

    while current_min <= current_max:
        if array[current_mid] == target:
            return True
        elif array[current_mid] < target:
            current_min = current_mid + 1
        else:
            current_max = current_mid - 1

        current_mid = (current_min + current_max) // 2

    return False
finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)