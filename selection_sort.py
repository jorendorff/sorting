import random
from console import ConsolePrinter
from sorter import Sorter

class SelectionSort(Sorter):
    def sort(self):
        for curstep in range(0, len(self.data)-1):
            lowest = curstep
            for i in range(curstep+1, len(self.data)):
                self.notify(self.data, [i], [curstep, len(self.data) - 1])
                if self.data[i] < self.data[lowest]:
                    lowest = i
        
            if i != curstep:
                self.data[curstep], self.data[lowest] = self.data[lowest], self.data[curstep]

        self.notify(self.data)

if __name__ == '__main__':
    num_list = range(0, 100)
    samples = random.sample(num_list, 40)

    printer = ConsolePrinter()
    selection = SelectionSort(samples)
    selection.registerObserver(printer)
    selection.sort()

