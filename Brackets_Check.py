class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peak(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def display(self):
        print self.stack


def check(data):
    s = Stack()
    i = 0

    while i < len(data) and s.is_empty != 0:
        if data[i] == "(":
            s.push(data[i])
        elif data[i] == ")":
            s.pop()
        i += 1

    if s.is_empty():
        return True
    else:
        return False


print(check('((()))'))
print(check('((()'))
