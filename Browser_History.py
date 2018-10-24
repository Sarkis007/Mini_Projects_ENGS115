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

class BH:
    def __init__(self):
        self.__backH = Stack()
        self.__fwdH = Stack()
        self.__current = ""

    def open(self, url):
        if self.__current is not "":
            self.__backH.push(self.__current)
            self.__fwdH = Stack()
        self.__current = url

    def back(self):
        if self.__backH.is_empty():
            print "No History:"
        else:
            self.__fwdH.push(self.__current)
            self.__current = self.__backH.pop()


    def fwd(self):
        if self.__fwdH.is_empty():
            print "No History:"
        else:
            self.__backH.push(self.__current)
            self.__current = self.__fwdH.pop()


    def printcurr(self):
        print self.__current


def main():
    bh = BH()
    bh.open("a")
    bh.open("b")
    bh.open("c")
    bh.printcurr()
    bh.back()
    bh.printcurr()
    bh.fwd()
    bh.printcurr()
    bh.fwd()
    bh.printcurr()
main()