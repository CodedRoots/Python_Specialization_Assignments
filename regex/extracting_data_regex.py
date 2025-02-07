# this code works with the file regex_sum_2104324.txt
# it reads the file, loop through the numbers and compute the sum of them

import re

fname = 'regex_sum_2104324.txt'
fhand = open(fname)
tot = 0

for line in fhand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if numbers:
        for nbr in numbers:
            nbr = int(nbr)
            tot = tot + nbr
print(tot)