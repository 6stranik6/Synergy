class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def sort_linked_list(head):
    if head is None or head.next is None:
        return head

    mid = get_middle(head)
    second_half = mid.next
    mid.next = None

    left = sort_linked_list(head)
    right = sort_linked_list(second_half)

    sorted_list = merge(left, right)
    return sorted_list

def get_middle(head):
    slow = head
    fast = head
    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left

    if left.value < right.value:
        result = left
        result.next = merge(left.next, right)
    else:
        result = right
        result.next = merge(left, right.next)

    return result

# Создаем список 4 -> 2 -> 1 -> 3
head = Node(4)
node2 = Node(2)
node1 = Node(1)
node3 = Node(3)
head.next = node2
node2.next = node1
node1.next = node3

# Сортируем список
head = sort_linked_list(head)

# Проверка результата
current = head
while current is not None:
    print(current.value)
    current = current.next