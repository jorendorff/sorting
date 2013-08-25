import random
from sorter import Sorter
from console import ConsolePrinter

class BubbleSort(Sorter):
    def sort(self):
        for curstep in range(len(self.data)-1, 0, -1):
            for i in range(curstep):
                self.notify(self.data, [i], [0, curstep])
                if self.data[i] < self.data[i +1]:
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]

        self.notify(self.data)

if __name__ == '__main__':
    num_list = range(0, 100)
    samples = random.sample(num_list, 40)

    printer = ConsolePrinter()
    bubble_sort = BubbleSort(samples)
    bubble_sort.registerObserver(printer)
    bubble_sort.sort()
