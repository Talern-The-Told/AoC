
from functions import *
print('Starting')

file = r'day7\data.txt'
data = organize_info(file)
total = []

ops = ['*','+']

list = get_all_problems(data,ops)
print('We got all the problems...')
for line in list:
    print(f"Going through line {line}")
    for equation in line:
        
        if ')||' in equation:           
            equation += (')'*equation.count(')||'))
            equation = equation.replace(')||','')
            
        if '||' in equation:
            equation = equation.replace('||','')


        print(eval(equation),equation)

        if eval(equation) is True:
            #print(eval(equation),equation)
            equation = equation.split('==')
            total.append(int(equation[0]))
            
        
print(f'The sum of the equations that work is {sum(set(total))}')
