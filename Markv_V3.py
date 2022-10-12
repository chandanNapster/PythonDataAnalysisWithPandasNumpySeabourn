import numpy as np
import re 

file = ['D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Gita.txt']

text = ""
for fl in file:
    with open(fl,'r', encoding='utf8') as txt:
        text += txt.read()
text = text[:500]
# STEP 0 -- USE OF REGEX TO CREATE BETTER TOKENS
text = re.sub("[^A-z,.!?\n ]", "", text)
print(text)

# STEP 1 -- EXTRACT ALL THE TOKENS THEN MAKE THEM DISTINCT AND THEN CREATE A DICTIONARY
tokens = text.lower().split()
distinct_tokens = list(set(tokens))
state_dict = dict([(data, index) for index, data in enumerate(distinct_tokens)])

# STEP 2 -- CREATE A MATRIX WITH TRANSITIONS
row, col = len(distinct_tokens),len(distinct_tokens)
trans_matrix = np.zeros((row, col))

# STEP 2.1 POPULATE THE TRANSITION MATRIX

for i in range(len(tokens) - 1):
    rw = state_dict[tokens[i]]
    co = state_dict[tokens[i+1]]
    trans_matrix[rw][co] += 1

# THIS CODE CHECKS THAT TRANSITION HAVE BEEN ASSIGNED A VALUE
# for i in range(row):
#     for j in range(col):
#         if trans_matrix[i][j] >= 1: print(i, j, trans_matrix[i][j])    

num_of_sentences = 0
current_state_index = np.random.randint(len(distinct_tokens))
current_state = distinct_tokens[current_state_index]
output = current_state + " "


while num_of_sentences <= 50:
    
    output += " "
    row = trans_matrix[state_dict[current_state], :]
    prob = row / row.sum()
    next_state_index = np.random.choice(len(distinct_tokens), 10, p = prob)
    # print(next_state_index)
    next_state = distinct_tokens[next_state_index[0]]

    if next_state[-1] in ['.','!','?']: 
        num_of_sentences += 1
        output += '\n'

    output += next_state
    current_state = next_state


# print(output)