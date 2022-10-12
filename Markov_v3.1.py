import numpy as np
import re

file = ['D:\OneDrive - BENNETT UNIVERSITY\BU\Reserach\Python Dev Work\PythonDataAnalysisWithPandasNumpySeabourn\Gita.txt']


text = ""
for fl in file:
    with open(fl, 'r', encoding='utf8') as txt:
        text += txt.read()


# IMPORVING THE TEXT WITH re

text = re.sub("[^A-z,.!?\n' ]+", "", text)
# THIS IS NEEDED FOR TOKENIZING THE PUNCUTATIONS THE \1 is called as the capture syntax and () are put on the re. 
# r is put in front of \1 so that it is interpreted as a raw string
text = re.sub("([.,!?])", r" \1 ", text)

# print(text)

tokens = text.lower().split()
distinct_tokens = list(set(tokens))
state_dict = dict([(data, index) for index, data in enumerate(distinct_tokens)])

row = len(distinct_tokens)
col = len(distinct_tokens)

my_matrix = np.zeros((row,col))

for i in range(len(tokens) - 1):
    rw = state_dict[tokens[i]]
    cl = state_dict[tokens[i+1]]
    my_matrix[rw][cl] += 1


current_state_index = np.random.randint(len(distinct_tokens))
current_state = distinct_tokens[current_state_index]
output = current_state + " "
num_of_sentences = 0

while num_of_sentences <= 3000:
    row_1 = my_matrix[[state_dict[current_state]],:]
    # print(row)
    row_1 = row_1.flatten()
    # row = row/1.0
    if row_1.sum() != 0:
        prob = row_1 / row_1.sum()
    my_matrix[[state_dict[current_state]],:] = prob 
    next_state_index = np.random.choice(len(distinct_tokens), 10, p=prob)
    next_state = distinct_tokens[next_state_index[0]]
    output += next_state
    output += " "
    # print(next_state)

    if next_state[-1] in ['.', '!', '?']:
        num_of_sentences += 1
        output += '\n'
    current_state = next_state

print(output)
# for i in range(row):
#     for j in range(col):
#         if 0 < my_matrix[i][j] < 1: print((i,j,my_matrix[i][j]))


   