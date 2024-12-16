import pandas as pd
import re
file = r'day9\test.txt'

with open(file,'r') as file:
    data =file.read()

formatted_data = []
#print(line)
id = 0
line =''

for i in range(0,len(data),2):

    block = (data[i])
    try:
        space = data[i+1]
    except:
        space =0
    #print(id,block,space)
    line += str(id) * int(block) + int(space)*'.'
    #print((str(id) * int(block)) + int(space)*'.')
    id +=1
length = len(line)-1

print(line)

for i in range(length,0,-1):

    if '.' not in line:
        break

    if line[i] != '.': # i is location of last digit
        #print(i,j)
        j = line.find('.') #find index of first .
        line = line[:j]+ line[i] + line[j+1:i]

        
print(line)
summup = 0
for i in range(0,len(line)):

    summup += i * int(line[i])
        #print(i,line[i])

print(summup)
