
def equation_possibilites(result,equation,ops):
    print('Getting possibilities')
    E1 = []
    from itertools import product

    for option in product(ops, repeat = len(equation)-1):
        
        #line = [f'{str(result)} == {equation[0]}']
        line = f'{equation[0]}'
        for i in range(1,len(equation)):
            j = i-1
            line = ''.join('(' + str(line) + option[j] + str(equation[i])+')')
            #line = ''.join(line)
        line = ''.join(f'{str(result)} ==' + line)
        E1.append(line)
        
        
    E2 = []

    for equation in E1:
        E2.append(''.join(equation))
    print(f'Returning possibilities for {equation}')
    return E2

def organize_info(file):
    print('Reading the file')
    data = []
    with open(file,'r') as file:
        for line in file:

            E1 = line.split('\n')
            E2 = E1[0].split(':')
            E3 = E2[1].split()
            data.append((E2[0],E3))
    print('Data gathered')
    return data

def get_all_problems(data,ops):
    print('getting problems')
    problems = []
    for equation in data:
        
        inputs = equation[1]
        result = equation[0]
        problems.append(equation_possibilites(result,inputs,ops))
        #print(equation,inputs,problems,'\n')
    print('returning problems')
    return problems


#the use temp total = eval(code)









#Each equation will have m^(n-1) possiblities.
# m = types of operators
# n = inputs into the equation

