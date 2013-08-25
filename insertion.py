import random
from console import ConsolePrinter
from sorter import Sorter

class InsertionSort(Sorter):
    def sort(self):
        j = 1
        data_size = len(self.data)

        while j < data_size:
            index = j - 1
            value = self.data[j]

            while index >= 0 and self.data[index] > value:
                self.notify(self.data, [index], [j, 0])
                self.data[index + 1] = self.data[index]
                index -= 1
                
            self.data[index + 1] = value
            j += 1

        self.notify(self.data)

if __name__ == '__main__':
    num_list = range(0, 100)
    samples = random.sample(num_list, 40)

    printer = ConsolePrinter()
    insertion_sort = InsertionSort(samples)
    insertion_sort.registerObserver(printer)
    insertion_sort.sort()
