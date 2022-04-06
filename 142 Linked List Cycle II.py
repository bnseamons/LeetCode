import math

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_val):
        new_node = Node(new_val)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, ref_node, val):
        if ref_node is None:
            return
        new_node = Node(val)
        new_node.next = ref_node.next
        ref_node.next = new_node

    def insert_at_end(self, new_val):
        new_node = Node(new_val)

        # If empty linked list is given
        if self.head is None:
            self.head = new_node
            return

        # Traversing the given LL to reach the end
        ref_node = self.head
        while ref_node.next:
            ref_node = ref_node.next
        ref_node.next = new_node

    def delete_key(self, key):
        temp = self.head

        # Checking if the key to be deleted is at the head
        if temp is not None:
            if temp.value == key:
                self.head = temp.next
                temp = None
                return

        # If the key isn't at the head
        # TRICK -> Assign first, check later. If check yields True, break and don't update.
        while temp is not None:
            if temp.value == key:
                break
            prev_node = temp
            temp = temp.next

        # If key isn't present in the linked list
        if temp is None:
            print("\nInvalid Entry! ")
            return

        prev_node.next = temp.next
        temp = None

    # Delete the first occurrence
    def delete_key_using_dummy(self, key):
        dummy_head = Node(-math.inf)
        dummy_head.next = self.head
        curr_node = dummy_head

        while curr_node.next is not None:
            if curr_node.next.value == key:
                curr_node.next = curr_node.next.next
                break
            else:
                curr_node = curr_node.next
        return dummy_head.next

    def delete_all_occurrences(self, key):
        dummy_head = Node(-math.inf)
        dummy_head.next = self.head
        curr_node = dummy_head

        while curr_node.next is not None:
            if curr_node.next.value == key:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next
        return dummy_head.next

    def print_linked_list(self):
        if self.head is None:
            return ""

        node = self.head
        while node:
            print(node.value, end="   ")
            node = node.next

    def length(self):
        curr_node = self.head
        count = 0
        while curr_node:
            count += 1
            curr_node = curr_node.next
        return count

    def search_key(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.value == key:
                return True
            else:
                curr_node = curr_node.next
        return False

    def search_key_recursive(self, node, key):
        if not node:
            return
        if node.value == key:
            return True
        return self.search_key_recursive(node.next, key)

    def get_at_index(self, index):
        curr_node = self.head
        if index > self.length() - 1:
            return -1
        for i in range(index):
            if curr_node:
                curr_node = curr_node.next
        return curr_node.value

    def n_from_end(self, n):
        curr_node = self.head
        if n > self.length():
            return -1
        index = self.length() - n
        for i in range(index):
            if curr_node:
                curr_node = curr_node.next
        return curr_node.value

    def n_from_end_runner(self, n):
        p1, p2, count = self.head, self.head, 0
        if self.head is not None:
            while count < n:
                if p2 is None:
                    return -1
                p2 = p2.next
                count += 1

        while p2 is not None:
            p1 = p1.next
            p2 = p2.next
        return p1.value

    def middle_val(self):
        p1, p2 = self.head, self.head
        if self.head:
            while p2 and p2.next:
                p1 = p1.next
                p2 = p2.next.next
        return p1.value

    def count_repetition(self, key):
        curr_node, count = self.head, 0
        while curr_node:
            if curr_node.value == key:
                count += 1
            curr_node = curr_node.next
        return count

    def detect_loop_hm(self):
        S, curr_node = set(), self.head
        while curr_node:
            if curr_node in S:
                return True
            S.add(curr_node)
            curr_node = curr_node.next
        return False

    # Floyd's Cycle Finding Algorithm
    def find_cycle(self):
        p1, p2 = self.head, self.head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    def reverse_linked_list(self):
        curr_node, prev, next = self.head, None, None
        while curr_node:
            # Making changes to the node
            next = curr_node.next
            curr_node.next = prev

            # Traversing through the Linked List
            prev = curr_node
            curr_node = next
        self.head = prev


def hasCycle(head):
    fast = head
    slow = head
    while fast != None and fast.next != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False



def detectCycle(head):
    #determine if there is a cycle
    fast = head
    slow = head
    hasCycle = False
    while fast.next != None and fast != None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            hasCycle = True
            break
    if hasCycle == False:
        return None
    # determine length of the cycle
    fast = fast.next
    length = 1
    while fast != slow:
        fast = fast.next
        length += 1
    fast = head
    slow = head
    while length > 0:
        fast = fast.next
        length -= 1
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast


node1 = Node(1)
current = node1
current.next = Node(2)
current = current.next
current.next = Node(3)
current = current.next
node2 = current
current.next = Node(4)
current = current.next
current.next = Node(5)
current = current.next
current.next = node2

detectCycle(node1)


