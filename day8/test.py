n_rows = 50+1
n_columns = 50+1

def boundary(set):
    bound = False
    if set[0] in range(0,n_rows):
        
        if set[1] in range(0,n_columns):
            
            bound = True
            return bound

for i in range(0,n_rows,1):
    print(i)