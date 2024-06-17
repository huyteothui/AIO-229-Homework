#EXERCISE 1

def sliding_window(num_list, k):
    result = []
    for i in range(len(num_list) - k + 1):
        max_num = 0
        for m in range(k):
            if num_list[i+m] < 1:
                pass
            else:
                if num_list[i+m] > max_num:
                    max_num = num_list[i+m]
        result.append(max_num)
    print(result)

#EXERCISE 2


def count_chars(string):
    unique_chars = []
    result = {}
    for letter in string:
        if letter not in unique_chars:
            unique_chars.append(letter)
            result[letter] = 1
        else:
            result[letter] += 1

#EXERCISE 3


def word_count(file_path):
    result = {}
    unique_words = []
    with open(file_path, "r") as file:
        content = file.readlines()
        for line in content:
            for word in line.split():
                if word not in unique_words:
                    unique_words.append(word)
                    result[word] = 1
                else:
                    result[word] += 1
    print(result)


#EXERCISE 4
def cost(i, j, source, target):
    if source[i - 1] == target[j - 1]:
        return 0
    else:
        return 1


def levenshtein(source, target):
    matrix = [[0 for _ in range(len(target) + 1)] for m in range(len(source) + 1)]
    for i in range(len(target) + 1):
        matrix[0][i] = i
    for i in range(len(source) + 1):
        matrix[i][0] = i
    for i in range(1, len(source) + 1):
        for j in range(1, len(target) + 1):
            matrix[i][j] = min(matrix[i - 1][j] + 1,
                               matrix[i][j - 1] + 1,
                               matrix[i - 1][j -1] + cost(i, j, source, target))
    print(matrix[len(source)][len(target)])	
