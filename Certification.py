import numpy as np

my_matrix = np.random.randint(-100,100, (5,5))

my_mat_arr = np.array(my_matrix)

# DISPLAY THE ARRAY
# print(my_mat_arr)

# # PYTHON CODE TO ACCESS A PARTICULAR RO5
# print("THE ROW IS")
# print(my_mat_arr[0])

# # PYTHON CODE TO ACCESS CERTAIN COL IN A PARTICULAR ROW
# print("COL OF A ROW")
# print(my_mat_arr[0][2:])

# # PYTHON CODE TO SLICE A SUB MATRIX FROM A BIGGER MATRIX
# print("SUB MATRIX")
# print(my_mat_arr[0:3])

# CODE TO REPLACE NEGATIVE NUMBER BY 0 AND ODD NUMBER BY -2
print(my_mat_arr)


my_new = my_mat_arr

my_mat_arr[my_mat_arr < 0] = 0
my_mat_arr[my_mat_arr % 2 != 0] = -2

print(my_mat_arr)


row, col = my_new.shape

for i in range(row):
    for j in range(col):
        if my_new[i][j] < 0:
            my_new[i][j] = 0
        elif my_new[i][j] % 2 != 0:
            my_new[i][j] = -2

print(my_new)