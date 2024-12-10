import pandas as pd

data = pd.read_csv('ReportData.txt', sep = ' ', engine='python', header = None)




    



Successful_Reports = 0



num_of_rows = range(len(data))

#num_of_rows = range(10)

for r in num_of_rows:
    Success = True

    abs_difference= 0 
    difference= 0

    original_row = data.loc[r].tolist()
    original_row = [x for x in original_row if str(x) != 'nan']
    num_of_columns = range(0,len(original_row))

        

    for c_dampened in num_of_columns:

        Success = True

        abs_difference= 0 
        difference= 0
       
        original_row = data.loc[r].tolist()
        row = [x for x in original_row if str(x) != 'nan']

        row.pop(c_dampened)
        num_of_damp_columns = range(1,len(row))

        for c in num_of_damp_columns:
            c_2 = c - 1
            #print(row)
            #print(row[c] - row[c_2])
            abs_difference += abs(row[c] - row[c_2])
            difference += row[c] - row[c_2]
            if row[c] - row[c_2]== 0:
                Success = False
                #print(f'Row {r}.{c_dampened}\n{original_row}\n{row} is unsuccessful: zero value')
                
                
            elif abs(row[c] - row[c_2]) > 3:
                Success = False
                #print(f'{r}.{c_dampened}\n{original_row}\n{row} is unsuccessful: More than 3')
            
            
        #print(abs_difference, difference)
        if abs_difference != abs(difference):
            #print(abs_difference, difference)
            #print(f'Row {r}.{c_dampened}\n{original_row}\n{row} is unsuccessful: change in direction')
            Success = False
            
        if Success:
            break


    if Success:
        print(f'row {r}.{c_dampened}:{row} is successful')
        Successful_Reports += 1



print(Successful_Reports)  
