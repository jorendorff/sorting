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

for curstep in range(len(samples)-1, 0, -1):
    os.system('cls' if os.name=='nt' else 'clear')
    for idx, sample in enumerate(samples):
        output = '{0}, {1}'.format(sample, sample*'|')
        if idx == curstep:
            print(Fore.RED + output)
        else:
            print(Fore.RESET + output)
    sleep(0.15)
    for i in range(curstep):
        os.system('cls' if os.name=='nt' else 'clear')
        for idxx in (range(curstep)):
            output = '{0}, {1}'.format(samples[idxx], samples[idxx]*'|')
            if i == idxx:
                print(Fore.GREEN + output)
            else:
                print(Fore.RESET + output)
        sleep(0.05)
        if samples[i] < samples[i +1]:
            samples[i], samples[i+1] = samples[i+1], samples[i]
print samples
