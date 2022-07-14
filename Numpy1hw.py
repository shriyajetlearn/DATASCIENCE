import numpy as np

matrix_1 = np.array([[45,89],[12,13]])
print(matrix_1)

matrix_2 = np.array([[23,90],[87,24]])
print(matrix_2)


#to add the matrices
add = np.add(matrix_1, matrix_2)
print(add)

#to subtract the matrices
sub = np.subtract(matrix_1, matrix_2)
print(sub)

#to calculate sum of all elements in one matrix
sum = 0;    
     
#Loop through the matrix to calculate sum of elements    
for i in range(0, len(matrix_1)):    
   sum = sum + matrix_1[i];    
     
print("Sum of all the elements of an matrix: " + str(sum));