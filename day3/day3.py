
file_path = r"C:\Users\tanne\OneDrive\Documents\GitHub\AdventOfCode\day3\data3.txt"

with open(file_path, "r") as data:
    string = data.read()
    #print(string)

import re

regex = (r"mul[(]\d\d?\d?,\d\d?\d?[)]")
mul = []
list()
mul=list((re.findall(regex, string)))
#print(mul)

def multiply(equation):
    multiples=[]
    multiples = re.findall(r'\d+',equation)
    multiples = [int(x) for x in multiples]
    value = multiples[0] * multiples[1]
    
    return value

value = 0
total = 0

for equation in range(len(mul)):
    #print(mul[equation])
    value = multiply(mul[equation])
    #print(value)
    total += value
    #print(total)
print(total)