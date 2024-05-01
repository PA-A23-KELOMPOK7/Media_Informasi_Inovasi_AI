import math

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.length = 0

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    def clear(self):
        self.head = None
        self.length = 0

    def QuickSortAsc(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x <= pivot]
            greater_than_pivot = [x for x in data[1:] if x > pivot]

            sorted = self.QuickSortAsc(less_than_pivot) + [pivot] + self.QuickSortAsc(greater_than_pivot)
            return  sorted

    def QuickSortDesc(self, data):
        if len(data) <= 1:
            return data
        else:
            pivot = data[0]

            less_than_pivot = [x for x in data[1:] if x >= pivot]
            greater_than_pivot = [x for x in data[1:] if x < pivot]

            sorted = self.QuickSortDesc(less_than_pivot) + [pivot] + self.QuickSortDesc(greater_than_pivot)
            return sorted
    
    def jumpSearch(self, id_post):
        current = self.head
        IdPost = []

        while current:
            IdPost.append(current.data[0])
            current = current.next

        IdPost = self.QuickSortAsc(IdPost)

        n = len(IdPost)
        step = int(math.sqrt(n))
        prev = 0

        while prev < n and IdPost[min(step, n) - 1] < id_post:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return None

        while IdPost[prev] < id_post:
            prev += 1
            if prev == min(step, n):
                return None

        if IdPost[prev] == id_post:
            current = self.head
            while current:
                if current.data['id_post'] == id_post:
                    return current
                current = current.next
            else:
                return False
