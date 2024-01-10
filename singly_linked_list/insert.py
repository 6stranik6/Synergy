class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def insert_after(node, new_value):
    if node is None:
        return
    
    new_node = Node(new_value)
    new_node.next = node.next
    node.next = new_node

head = Node(1)
node2 = Node(2)
node4 = Node(4)
head.next = node2
node2.next = node4

# Вставляем элемент со значением 3 после элемента со значением 2
insert_after(node2, 3)

# Создание узлов списка
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Связывание узлов в список
node1.next = node2
node2.next = node3

# Вызов функции insert_after для вставки нового узла со значением 4 после узла со значением 2
insert_after(node2, 4)

# Проверка результата
current = node1
while current is not None:
    print(current.value)
    current = current.next