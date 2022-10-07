
import os
from numpy import dtype
from scipy.sparse import csr_matrix

# current_dir = os.getcwd()

# print(current_dir)

# directories = os.listdir(current_dir)

# new_dir = ''
# new_paths = []
# for dir in directories:
#     new_path = current_dir + "\\" + dir  
#     new_paths.append(new_path)


# file_loc = new_paths[-1] + "\\Gita"

files = []

file_loc_1 = "E:\PythonWorkbook\PythonDataAnalysisWithPandasNumpySeabourn\Gita.txt"

files.append(file_loc_1)

text = ""
for file in files:
    with open(file, 'r') as t:
        text += t.read() 
tokens = text.lower().split()
distinct_states = list(set(tokens))

# print(len(distinct_states))

row = len(distinct_states)
col = len(distinct_states)

# print(row, col)

# TRANSITION MATRIX

m = csr_matrix(
    (row, col), 
    dtype=int
)

state_index = {}


# CAN BE USED TO CREATE A LIST OF TUPLES FROM A LIST
# REALLY HELPFUL FOR CREATING A KEY VALUE PAIR
state_list = [(index, d_state) for index,d_state in enumerate(distinct_states)]
    
# print(state_list)
state_index = dict(state_list)   
print(state_index) 

# COUNT THE TRANSITIONS
print(state_index[0]) 

m[0,1] += 1

print(m[0,1])

