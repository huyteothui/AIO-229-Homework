import numpy as np
from math import sqrt
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

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

### Question 4
def compute_correlation_coefficient(x, y):
    n = len(x)
    numerator = 0
    denominator = 0

    std_x = compute_std(x) 
    std_y = compute_std(y)

    mean_x = compute_mean(x)
    mean_y = compute_mean(y)

    temp_total = 0
    for i in range(n):
        temp_total += ((x[i] - mean_x) * (y[i] - mean_y))
    
    numerator = temp_total / n

    denominator += std_x * std_y
    
    return numerator / denominator

# Cau 10
def tfidf_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(context_embedded, query_embedded).reshape((-1,))
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'cosine_score':cosine_scores[idx]
        }
        results.append(doc)
    return results

#Cau 12
def tfidf_search(question, tfidf_vectorizer, top_d=5):
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(context_embedded, query_embedded).reshape((-1,))
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'cosine_score':cosine_scores[idx]
        }
        results.append(doc)
    return results
