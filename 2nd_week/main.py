from structures import ListNode, LinkedList

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

linked_list.remove(3)

print(linked_list.get(2).val)
print(linked_list.get(3))