class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = None

    def push(self, x):
        self.stack.append(x)
        if self.min is None or x < self.min:
            self.min = x

    def pop(self):
        num = self.stack[len(self.stack) - 1]
        self.stack.pop(len(self.stack) - 1)

        if len(self.stack) == 0:
            self.min = None
        else:
            if self.min == num:
                self.min = self.stack[0]
                if len(self.stack) > 1:
                    for i in range(1, len(self.stack)):
                        if self.min > self.stack[i]:
                            self.min = self.stack[i]

    def top(self):
        return self.stack[len(self.stack) - 1]

    def getMin(self):
        return self.min

obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
obj.pop()
print(obj.getMin())
