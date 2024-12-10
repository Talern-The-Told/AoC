import pandas as pd

data = pd.read_csv('ReportData.txt', sep = ' ', engine='python', header = None)
Diff_list = []

for r in range(len(data)):
    row = data.loc[r].tolist()
    row_result = []
    #print(row)
    for c in range(1,len(row)):
        prev_column = c - 1
        #print(row[c])
        value = row[c] - row[prev_column]
        row_result.append(value)
        
    Diff_list.append(row_result)



    

df_diff = pd.DataFrame(Diff_list)

Successful_Reports = 0



num_of_rows = range(len(df_diff))

num_of_rows = range(10)

for r in num_of_rows:
    Success = True
    #negative = False
    #next_negative = False  
    abs_difference= 0 
    difference= 0
    #og_data = print(data.loc[r].tolist())
    #row = df_diff.loc[r].tolist()
    row = data.loc[r].tolist()
    row = [x for x in row if str(x) != 'nan']
    num_of_columns = range(1,len(row))



    sum_of_row = abs(sum(row))
    abs_row = [abs(ele) for ele in row]
    abs_sum = sum(abs_row)

    '''if sum_of_row != abs_sum:
        was_positive = True
        Success = False
        print(f'{row} is unsuccessful: change in direction')
        print(sum_of_row,abs_sum)'''
        

    for c in num_of_columns:
        c_2 = c - 1
        
        abs_difference += abs(row[c] - row[c_2])
        difference += row[c] - row[c_2]
        if row[c] - row[c_2]== 0:
            Success = False
            #print(f'row {r}:{row} is unsuccessful: zero value')
            
            
        if abs(row[c] - row[c_2]) > 3:
            Success = False
            #print(f'row {r}:{str(row)} is unsuccessful: More than 3')
        
        
        
    if abs_difference != abs(difference):
        #print(abs_difference, difference)
        print(f'{row} is unsuccessful: change in direction')
        Success = False


    if Success:
        print(f'row {r}:{row} is successful')
        Successful_Reports += 1



print(Successful_Reports)  
