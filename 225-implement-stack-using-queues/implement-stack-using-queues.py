from collections import deque

class MyStack:

    def __init__(self):
        self.queue = deque([])

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        temp_queue = deque([])
        while len(self.queue) > 1:
            temp_queue.append(self.queue.popleft())
        result = self.queue.popleft()
        while len(temp_queue):
            self.queue.append(temp_queue.popleft())
        return result

    def top(self) -> int:
        temp_queue = deque([])
        while len(self.queue) > 1:
            temp_queue.append(self.queue.popleft())
        result = self.queue.popleft()
        temp_queue.append(result)
        while len(temp_queue):
            self.queue.append(temp_queue.popleft())
        return result

    def empty(self) -> bool:
        if len(self.queue):
            return False
        return True
            


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()