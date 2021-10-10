import sys
import re
import json

sample = {'Object': 1629,  'Point': 1675, 'Rectangle': 2042}

filename = 'test.txt'

with open(filename) as file:
    while (line := file.readline().rstrip()):
       line = re.sub('John','Jim', line)
       print(line)


with open('result.json', 'w') as file:
    json_string = json.dumps(sample, default=lambda o: o.__dict__, sort_keys=True, indent=2)
    file.write(json_string)


with open('result.json') as json_file:
    data = json.load(json_file)


print(data)

