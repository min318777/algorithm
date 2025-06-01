shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]


def is_available_to_order(menus, orders):
    menus.sort()

    for menu in orders:

        min_num = 0
        max_num = len(menus) - 1

        found = False

        while min_num <= max_num:
            mid_num = (min_num + max_num) // 2
            if menus[mid_num] == menu:
                found = True
                break
            elif menus[mid_num] < menu:
                min_num = mid_num + 1
            else:
                max_num = mid_num - 1


    if found:
        return True

    return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)