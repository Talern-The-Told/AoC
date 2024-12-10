#Day one
import pandas as pd

data = pd.read_csv('day1data.csv', sep = '   ', engine='python', header = None)

data.columns = ['List_1','List_2']


List_1 = data['List_1'].tolist()
List_2 = data['List_2'].tolist()
List_1.sort()
List_2.sort()
sum = 0


for i in range(len(List_1)):
    sum = sum + abs( List_1[i] - List_2[i] )
    #print(sum)
    



print(f'The sum of differences between list 1 and list 2 is {sum}')