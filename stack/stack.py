class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
priority = {'(': 1, ')': 1, '+': 2, '-': 2, '*': 3, '/': 3}
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node

    def pop(self):
        if self.top is None:
            return None
        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
