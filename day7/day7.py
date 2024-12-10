file = r'day7\test.txt'
data = []
with open(file,'r') as file:
    for line in file:
        E1 = line.split('\n')
        E2 = E1[0].split(':')

        data.append(E2)

import operator

operator_functions = {
    '+': operator.add, 
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}


print(data)
operators = ['+','*']
for equation in data:
    result = equation[0]
    values = equation[1].split()
    print(result,values)
    tested_total = 0
    while tested_total != result:
        for i in len(values):
            answer  =operator_functions[op,values[i],,values[i+1])
