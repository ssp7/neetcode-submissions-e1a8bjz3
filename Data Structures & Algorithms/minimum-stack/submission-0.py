class MinStack:

    def __init__(self):
        self.nums = []
        self.stack = []

    def push(self, val: int) -> None:
        self.nums.append(val)
        if self.stack:
            minVal = min(self.stack[-1], val)
            self.stack.append(minVal)
        else:
            self.stack.append(val)

    def pop(self) -> None:
        self.nums.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.stack[-1]
