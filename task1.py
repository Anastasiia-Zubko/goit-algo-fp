class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = Node(data)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def search_element(self, data) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Function to reverse the linked list
def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

# Function to merge two sorted linked lists
def merge_sorted_lists(l1, l2):
    temp = Node(0)
    tail = temp

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return temp.next

# Function to get the middle of the linked list
def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# Function to sort the linked list using merge sort
def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = merge_sorted_lists(left, right)
    return sorted_list


if __name__ == "__main__":
    # Create a linked list
    llist = LinkedList()
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    print("Original Linked List:")
    llist.print_list()

    # Reverse the linked list
    llist.head = reverse_linked_list(llist.head)
    print("\nReversed Linked List:")
    llist.print_list()

    # Sort the linked list
    llist.head = merge_sort_linked_list(llist.head)
    print("\nSorted Linked List:")
    llist.print_list()

    # Create two sorted linked lists for merging
    llist1 = LinkedList()
    llist1.insert_at_end(1)
    llist1.insert_at_end(3)
    llist1.insert_at_end(5)

    llist2 = LinkedList()
    llist2.insert_at_end(2)
    llist2.insert_at_end(4)
    llist2.insert_at_end(6)

    # Merge two sorted linked lists
    merged_head = merge_sorted_lists(llist1.head, llist2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head
    print("\nMerged Sorted Linked List:")
    merged_list.print_list()
