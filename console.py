import os
from colorama import init, Fore
from time import sleep

class ConsolePrinter(object):
    def __init__(self, delay = 0.05):
        self.clear = 'cls' if os.name == 'nt' else 'clear'
        self.delay = delay
        init()

    def notify(self, data, inspecting, boundaries):
        os.system(self.clear)

        for idx in range(0, len(data)):
            output = '{0: 3d}, {1}'.format(data[idx], data[idx]*'|')
            if idx in boundaries:
                print(Fore.RED + output)
            elif idx in inspecting:
                print(Fore.GREEN + output)
            else:
                print(Fore.RESET + output)

        sleep(self.delay)
