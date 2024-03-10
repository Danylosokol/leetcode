class MinStack:

    def __init__(self):
        self.stack = []


    def push(self, val: int) -> None:
        if self.stack:
            prev_node = self.stack[-1]
            prev_min = prev_node['min_val']
            curr_min = prev_min if val > prev_min else val
            self.stack.append({'val': val, 'min_val': curr_min})
        else:
            self.stack.append({'val': val, 'min_val': val})


    def pop(self) -> None:
        last_node = self.stack.pop()
        return last_node['val']


    def top(self) -> int:
        last_node = self.stack[-1]
        return last_node['val']


    def getMin(self) -> int:
        last_node = self.stack[-1]
        return last_node['min_val']
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()