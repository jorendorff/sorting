import random
import os
from time import sleep

from colorama import init, Fore
init()

num_list = range(0, 100)

samples = random.shuffle(num_list)
samples = random.shuffle(num_list)

samples = random.sample(num_list, 40)
print samples

for curstep in range(0, len(samples)-1):
    os.system('cls' if os.name=='nt' else 'clear')
    for idx in range(0, len(samples)-1):
        output = '{0}, {1}'.format(samples[idx], samples[idx]*'|')
        if idx == curstep:
            print(Fore.RED + output)
        else:
            print(Fore.RESET + output)
    sleep(0.25)
    lowest = curstep
    for i in range(curstep+1, len(samples)):
        os.system('cls' if os.name=='nt' else 'clear')
        for idxx in range(0, len(samples)-1):
            output = '{0}, {1}'.format(samples[idxx], samples[idxx]*'|')
            if i == idxx:
                print(Fore.GREEN + output)
            else:
                print(Fore.RESET + output)
        sleep(0.05)
        if samples[i] < samples[lowest]:
            lowest = i
    if i != curstep:
        samples[curstep], samples[lowest] = samples[lowest], samples[curstep]
print samples
