#Super template
class adoptable:
    def __init__(self):
        return self
    def __init_subclass__(self):
        return self
    def adopted(self):
        return self
class adopting(adoptable):
    def __init__(self):
        super(adopting, self).__init__()

parent = adopting()

parent.adopted()