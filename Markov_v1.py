import re 
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix


file = ["D:\OneDrive - BENNETT UNIVERSITY\Desktop\Python Workbook\Gita.txt"]

text = ""
for book_file in file:
    with open(book_file, 'r',encoding='utf8') as txt:
        text += txt.read()


tokens = text.lower().split()
distinct_states = list(set(tokens))
row, col = len(distinct_states), len(distinct_states)

m = csr_matrix((row,col), dtype=int)
my_mat = np.zeros((row,col))
# LOTS OF STUFF IS GOING ON HERE

state_index = dict([(data_val, index) for index, data_val in  enumerate(distinct_states)])
# print(state_index)

# print(text)
# print(tokens)

for i in range(len(tokens) - 1):
    # print("First word is [{0}] and the second word is [{1}]".format(tokens[i], tokens[i+1]))
    row = state_index[tokens[i]]
    col = state_index[tokens[i + 1]]
    my_mat[row][col] += 1



start_state_index = np.random.randint(len(distinct_states))
start_state = distinct_states[start_state_index]
output = start_state + " "
num_of_sentences = 0

while num_of_sentences <= 30:
    row = my_mat[state_index[start_state], :]
# print(start_state)
# print(row)
# print(row)
# row[2] = .34
# row[1] = .56
# row[4] = .77
    probabilities = row / row.sum()
# probabilities = np.array(probabilities)

# print(probabilities)


    next_state_index = np.random.choice(len(distinct_states), 1, p = probabilities)

    next_state = distinct_states[next_state_index[0]]
    output += next_state 
    output += " "
    if next_state[-1] in ['.','!', '?']:
        num_of_sentences += 1
        output += "\n"
    start_state = next_state

print(output)

# print(next_state)

# print(my_mat)

# print(text)

# tup = []
# for i in range(row):
#     for j in range(col):
#         if my_mat[i][j] >= 1.0:
#             tup.append((i,j, my_mat[i][j]))
            










# for i in range(len(tokens)-1):
#     row = state_index[tokens[i]]
#     col = state_index[tokens[i + 1]]
#     m[row,col] += 1

# print("THE MESSAGE")
# # print(text)
# # print(state_index)
# print(m)

