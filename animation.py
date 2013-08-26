""" Show a movie illustrating the operation of a sorting algorithm. """

import random, os, time, colorama

colorama.init()

clear_cmd = 'cls' if os.name == 'nt' else 'clear'
delay = 0.01

def matches(i, region):
    """ True if the int i falls in the given region (an int or a slice). """
    if isinstance(region, int):
        return i == region
    elif isinstance(region, slice):
        return region.start <= i < region.stop
    else:
        return False

def paint(data, get_region=None, set_region=None):
    os.system(clear_cmd)
    for i in range(0, len(data)):
        output = '{0: 3d}, {1}'.format(data[i], data[i]*'=')
        if matches(i, get_region):
            print(colorama.Back.GREEN + output)
        elif matches(i, set_region):
            print(colorama.Back.RED + output)
        else:
            print(colorama.Back.RESET + output)
    print(colorama.Back.RESET)
    time.sleep(delay)

class IllustratedList(object):
    """ A list that calls paint() whenever elements are accessed. """
    def __init__(self, data):
        self._data = list(data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        paint(self._data, get_region=index)
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value
        paint(self._data, set_region=index)

def play_sorting_movie(algorithm):
    src = list(range(40))
    random.shuffle(src)
    my_data = IllustratedList(src)
    algorithm(my_data)

    # paint again without highlighting
    paint(my_data._data)
