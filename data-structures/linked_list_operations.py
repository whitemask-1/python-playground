class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        if self.head is None:
            print("[]")
        else:
            arr = []
            last = self.head
            while last is not None:
                arr.append(last.value)
                last = last.next
            return " ".join(str(n) for n in arr)
    # O(n)
    def __contains__(self, search):
        last = self.head
        while last is not None:
            if last.value == search:
                return True
            last = last.next
        return False

    # O(n)
    def __len__(self):
        count = 0
        last = self.head
        while last is not None:
            count += 1
            last = last.next
        return count


    # O(n)
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1)
    def prepend(self, value):
        first_node = Node(value)
        first_node.next = self.head
        self.head = first_node

    # O(n)
    def insert(self, value, index):
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise IndexError("Index out of bounds")
            else:
                last = self.head

                for _ in range(index-1):
                    if last.next is None:
                        raise IndexError("Index out of bounds")
                    last = last.next

                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node
    # O(n)
    def delete(self, value):
        last = self.head

        if last.next is not None:
            if last.next.value == value:
                last.next = last.next.next

    # O(n)
    def pop(self, index):
        if self.head is None:
            raise IndexError("Index out of bounds")
        else:
            last = self.head

            for _ in range(index - 1):
                if last.next is None:
                    raise IndexError("Index out of bounds")
                last = last.next

            if last.next is None:
                raise IndexError("Index out of bounds")
            else:
                last.next = last.next.next

    # O(n)
    def get(self, index):
        if self.head is None:
            raise IndexError("Index out of bounds")
        else:
            last = self.head
            for _ in range(index):
                if last.next is None:
                    raise IndexError("Index out of bounds")
                last = last.next
            return last.value

    def print(self):
        pass

newlist = LinkedList()
newlist.append(20)
newlist.append(30)

print(newlist.__repr__)
