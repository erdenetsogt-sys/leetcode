class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        if len(self.stack2) == 0:
            self.stack2.append(x)
        else:
            for i in range(len(self.stack2)):
                self.stack.append(self.stack2.pop())
            self.stack.append(x)
            for i in range(len(self.stack)):
                self.stack2.append(self.stack.pop())

    def pop(self) -> int:
        if len(self.stack2) != 0:
            return self.stack2.pop()

    def peek(self) -> int:
        if len(self.stack2) != 0:
            return self.stack2[-1]

    def empty(self) -> bool:
        return len(self.stack2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()