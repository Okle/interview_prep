class node:
    def __init__(self, val):
        self.data = val
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
        self.lastNode = None

    def insert(self, val):

        if self.head is None:
            self.head = node(val)
            self.lastNode = self.head
        else:
            # temp = self.head
            # while temp.next:
            #     temp = temp.next
            #
            # temp.next = node(val)
            new_node = node(val)
            self.lastNode.next = new_node
            self.lastNode = new_node

    def remove(self, val):

        if self.head.data == val:
            self.head = self.head.next
            return

        curr = self.head
        while curr.next.data != val:
            curr = curr.next

        curr.next = curr.next.next

    def reverseList(self):
        # Code here
        if self.head is None:
            return None

        curr = self.head
        curr_next = self.head.next
        while curr:
            if curr_next == self.lastNode:
                curr_next.next = curr
                break
            else:
                temp = curr_next
                curr_next = curr_next.next
                temp.next = curr
                curr = temp

    def createList(self, arr):

        for i in range(len(arr)):
            self.insert(node(arr[i]))
        return self.head

    def printList(self):

        curr = self.head
        while curr is not None:
            print(curr.data, end=' ')
            curr = curr.next

    def reverseList(self):

        if self.head is None or self.head.next is None:
            return None

        curr = self.head
        curr_next = self.head.next
        while curr:
            if curr_next == self.lastNode:
                curr_next.next = curr
                break
            else:
                temp = curr_next
                curr_next = curr_next.next
                temp.next = curr
                curr = temp

        temp = self.lastNode
        self.lastNode = self.head
        self.lastNode.next = None
        self.head = temp



def findMid(head):
    # Code here

    if head is None:
        return -1

    if head.next is None:
        return head.data

    index_dict = {}
    count = 1
    curr = head
    while curr.next:
        count += 1
        index_dict[count] = curr.next
        curr = curr.next
    return index_dict.get(count // 2 + 1)


def findMid_slow_fast(head):
    # Code here

    if head is None:
        return -1

    curr_slow = head
    curr_fast = head
    while curr_fast.next:
        curr_slow = curr_slow.next
        if curr_fast.next.next is None:
            break
        curr_fast = curr_fast.next.next

    return curr_slow

