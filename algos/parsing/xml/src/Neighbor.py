class Neighbor:
    def __init__(self, name, direction):
        self.name = name
        self.direction = direction

    def __iter__(self):
        return [self.name, self.direction]
