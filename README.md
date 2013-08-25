# Sorting

There are tons of different sorting methods available.  Reading about
them is one thing; watching them run is something entirely different.
This project allows you to easily watch as various sorting algorithms
perform their magic, helping you to gain a better understanding of how
they work.

# Setup

Getting started with this project is as easy as

    git clone https://github.com/jasonamyers/sorting.git
    cd sorting
    pip install -r requirements.txt
    python <filename_of_algorithm>

# Contribute

If you would like to add an additional sorting mechanism, create a
class that inherits from Sorter and implements a method sort().
Whenever the data changes, call the notify method with the following
arguments:

* self.data :: This contains the list of values currently being sorted
* inspecting :: This is a list of the current indices that are
  actively being used.  Typically this is only one value, but there
  are sorting algorithms where this may not be true.
* boundaries :: This is a list containing the bounding indices of the
  current inspection, useful to show how the algorithm divides us
  lists for more efficient processing

A skeleton for a new sorting class has been included below for your
convenience.

    import random
    from sorter import Sorter
    from console import ConsolePrinter
        
    class MySort(Sorter):
        def sort(self):
            # Implement your sorting algorithm here
            self.notify(self.data, [index], [lower_bound, upper_bound])
        
    if __name__ == '__main__':
        num_list = range(0, 100)
        samples = random.sample(num_list, 40)
    
        printer = ConsolePrinter()
        my_sort = MySort(samples)
        my_sort.registerObserver(printer)
        my_sort.sort()
