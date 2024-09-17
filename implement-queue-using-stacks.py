class MyQueue:

    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.insert(0, x)

    def pop(self) -> int:
        new_queue = []
        while not self.empty():
            current = self.queue.pop(0)
            if self.empty():
                self.queue = new_queue[::-1]
                return current
            new_queue.insert(0, current)

    def peek(self) -> int:
        new_queue = []
        current = None
        while not self.empty():
            current = self.queue.pop(0)
            new_queue.insert(0, current)
        self.queue = new_queue[::-1]
        return current

    def empty(self) -> bool:
        return not self.queue



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
