class MyQueue:

    def __init__(self):
        self._lst = []

    def push(self, x: int) -> None:
        self._lst.append(x)

    def pop(self) -> int:
        return self._lst.pop(0)

    def peek(self) -> int:
        return self._lst[0]

    def empty(self) -> bool:
        return len(self._lst) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()