class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(head, target):
    if head is None:
        return head

    if head.value == target:
        return head.next
    
    current = head
    while current.next is not None:
        if current.next.value == target:
            current.next = current.next.next
            return head
        current = current.next

    return head

# Создание узлов списка
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

# Связывание узлов в список
node1.next = node2
node2.next = node3
node3.next = node4

# Вызов функции delete_node для удаления узла со значением 3
new_head = delete_node(node1, 3)

# Проверка результата
current = new_head
while current is not None:
    print(current.value)
    current = current.next