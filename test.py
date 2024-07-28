import numpy as np
from numpy.linalg import norm
def compute_cosine(v1, v2):
    cos_sim = v1.dot(v2) / (norm(v1) * norm(v2))
    return cos_sim

x = np. array ([1 , 2 , 3 , 4])
y = np. array ([1 , 0 , 3 , 0])
result = compute_cosine (x,y)
print ( round (result , 3) )