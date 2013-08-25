class Observable(object):
    def __init__(self):
        self.observers = []

    def registerObserver(self, observer):
        if not observer in self.observers:
            self.observers.append(observer)

    def notify(self, data, inspecting = [], boundaries = []):
        for observer in self.observers:
            observer.notify(data, inspecting, boundaries)
