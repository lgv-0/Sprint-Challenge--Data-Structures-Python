class RingBuffer:
    def __init__(self, capacity):
        self.container = [None] * capacity
        self.capacity = capacity
        self.index = 0

    def append(self, item):
        self.container[self.index] = item

        self.index += 1

        if (self.index == self.capacity):
            self.index = 0

    def get(self):
        retbuild = []

        for item in self.container:
            if item is not None:
                retbuild.append(item)

        return retbuild