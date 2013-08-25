from observable import Observable

class Sorter(Observable):
    def __init__(self, data):
        super(Sorter, self).__init__()
        self.data = data
