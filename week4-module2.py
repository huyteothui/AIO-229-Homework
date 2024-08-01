import numpy as np
from math import sqrt

### Question 1
def compute_mean(arr: np.array):
    n = np.shape(arr)[0]
    x = np.sum(arr)
    return x / n

### Question 2
def compute_median(arr: np.array):
    n = int(np.shape(arr)[0] / 2)
    temp_arr = np.sort(arr)
    x1 = temp_arr[n]
    x2 = temp_arr[n-1]
    return(x1 + x2) / 2

### Question 3
def compute_std(arr: np.array):
    mean = compute_mean(arr)
    n = np.shape(arr)[0]
    values = []
    for x in arr:
        values.append((x - mean) ** 2)
    return sqrt(sum(values) / n)