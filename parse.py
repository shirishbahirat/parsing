import sys
import re


filename = 'test.txt'



with open(filename) as file:
    while (line := file.readline().rstrip()):
       line = re.sub('John','Jim', line)
       print(line)
