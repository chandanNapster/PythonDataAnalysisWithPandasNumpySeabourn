import numpy as np

files = ['E:\PythonWorkbook\PythonDataAnalysisWithPandasNumpySeabourn\Gita.txt']

text = ""
for f in files:
    with open(f, 'r') as t: 
        text += t.read()

text = text[:150]

# TOKEN GENERATION
# TOKEN ARE DISTINCT
distinct_tokens = list(set(text.lower().split()))

# CREATE A DISTIONARY OF DISTINCT TOKENS
dict_list = dict([(data, index) for index, data in enumerate(distinct_tokens)])

print(dict_list)

count = 0
for item in distinct_tokens:
    print(dict_list.get(distinct_tokens[count]), dict_list.get(distinct_tokens[count]))
    count += 1

row = len(distinct_tokens)
col = row

my_matrix = np.zeros((row, col))

print(my_matrix)

my_matrix[1,1] = 0.45
my_matrix[2,1] = 0.23
my_matrix[3,4] = 0.65
my_matrix[dict_list['characters'], dict_list['one']] = 0.87
print("after")
print(my_matrix)

print(dict_list)

print(my_matrix[dict_list['characters'], dict_list['one']])