class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_num = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.min_num is None or self.min_num>x:
            self.min_num=x
        self.data.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.min_num == self.data[-1]:
            if len(self.data)>1:
                self.min_num = min(self.data[:-1])
            else:
                self.min_num = None
        return self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_num


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-1)
print(obj.getMin())
print(obj.top())
print(obj.pop())
print(obj.getMin())
