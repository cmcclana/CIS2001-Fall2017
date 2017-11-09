class PriorityQueueADT:
    def add(self, key, value):
        raise NotImplementedError

    def min(self):
        raise NotImplementedError

    def remove_min(self):
        raise NotImplementedError

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        raise NotImplementedError