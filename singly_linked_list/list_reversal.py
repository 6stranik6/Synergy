class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverse_linked_list(head):
    previous = None
    current = head
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

# Создание узлов списка
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Связывание узлов в список
node1.next = node2
node2.next = node3

# Вызов функции reverse_linked_list для разворота списка
reversed_head = reverse_linked_list(node1)

# Проверка результата
current = reversed_head
while current is not None:
    print(current.value)
    current = current.next