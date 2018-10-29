class Stack:
    def __init__(self):
        self.stack = []
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()
    def push(self,val):
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

class StackSort:
    def __init__(self):
        self.input = Stack()
        self.output = Stack()
        self.tmp = Stack()

    def sort(self, data):
        for i in data:
            self.input.push(i)
        while self.input.is_empty() == False:
            self.tmp = self.input.peak()
            self.input.pop()
            while self.output.is_empty() == False and int(self.output.peak()) < int(self.tmp):
                self.input.push(self.output.peak())
                self.output.pop()
            self.output.push(self.tmp)
        self.output.display()

def main():

    sortdata = StackSort()
    sortdata.sort((7,2,9,4,0,5))

main()