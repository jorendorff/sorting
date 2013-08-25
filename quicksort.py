import random
from sorter import Sorter
from console import ConsolePrinter

class QuickSort(Sorter):
    def sort(self):
        self._quicksort(0, len(self.data) - 1)
        self.notify(self.data)

    def _partition(self, left, right, pivot):
        pivotValue = self.data[pivot]
        self._swap(right, pivot)
 
        store = left
        for idx in range(left, right):
            if self.data[idx] < pivotValue:
                self._swap(idx, store)
                store += 1
                self.notify(self.data, [idx], [left, right - 1])
 
        self._swap(store, right)
        return store

    def _quicksort(self, left, right):
        if right > left:
            pivot = random.randint(left, right)
            pivot = self._partition(left, right, pivot)
            self._quicksort(left, pivot)
            self._quicksort(pivot + 1, right)


    def _swap(self, left, right):
        self.data[left], self.data[right] = self.data[right], self.data[left]

if __name__ == '__main__':
    num_list = range(0, 100)
    samples = random.sample(num_list, 40)

    printer = ConsolePrinter()
    quick_sort = QuickSort(samples)
    quick_sort.registerObserver(printer)
    quick_sort.sort()
