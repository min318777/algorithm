class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)


def get_linked_list_sum(linked_list_1, linked_list_2):                      # 내가푼 안좋은 방법
    num1 = ""
    num2 = ""
    cur = linked_list_1.head
    cur2 = linked_list_2.head
    while cur is not None:
        num1 += str(cur.data)
        cur = cur.next
    while cur2 is not None:
        num2 += str(cur2.data)
        cur2 = cur2.next

    return int(num1) + int(num2)

def get_single_linked_list_sum(linked_list):

    sum = 0

    cur = linked_list.head
    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum

def get_linked_list_sum2(linked_list_1, linked_list_2):

    sum1 = get_single_linked_list_sum(linked_list_1)
    sum2 = get_single_linked_list_sum(linked_list_2)

    return sum1 + sum2


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum2(linked_list_1, linked_list_2))