import numpy as np
from numpy.linalg import norm
#Exercise 1

# (a)
def compute_vector_length(vector):
    return np.sqrt(np.sum([v ** 2 for v in vector]))

# (b)
def compute_dot_product(vector1, vector2):
    return vector1.dot(vector2)

# (c)
def matrix_multi_vector(matrix, vector):
    return matrix.dot(vector)

# (d)
def matrix_multi_matrix(matrix1, matrix2):
    return np.matmul(matrix1, matrix2)

# (e)
def inverse_matrix(matrix):
    return np.linalg.inv(matrix)

#EXERCISE 2

def compute_eigenvalues_eigenvectors(matrix):
    return np.linalg.eig(matrix)

#EXERCISE 3

def compute_cosine(v1, v2):
    cos_sim = v1.dot(v2) / (norm(v1) * norm(v2))
    return cos_sim
