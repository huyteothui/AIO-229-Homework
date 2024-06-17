from random import uniform
from math import sqrt, e

# Exercise 1


def exercise1(tp, fp, fn):
    if type(tp) is not int:
        print("tp must be int")
        return
    if type(fp) is not int:
        print("fp must be int")
        return
    if type(fn) is not int:
        print("fn must be int")
        return
    if fn <= 0 or fp <= 0 or tp <= 0:
        print("tp and fp and fn must be greater than zero")
        return
    p = tp/(tp+fp)
    r = tp / (tp + fn)
    print(f"precision is {p}")
    print(f"recall is {r}")
    print("f1-score is", end=" ")
    print(2 * ((p * r)/(p + r)))

# EXERCISE 2


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def sigmoid(x):
    return 1 / (1 + e ** (-x))


def relu(x):
    if x <= 0:
        return 0
    else:
        return x


def elu(x, a=0.001):
    if x <= 0:
        return a * ((e ** x) - 1)
    else:
        return x


def exercise2():
    available_func = ["sigmoid", "relu", "elu"]
    x = input("Input x = ")
    if not is_number(x):
        print("x must be a number")
        return
    x = float(x)
    func = input("Input activation function (sigmoid|relu|elu): ").lower()
    if func not in available_func:
        print(f"{func} is not supported")
        return
    if func == "sigmoid":
        print(f"Sigmoid: f({x}) = {sigmoid(x)}")
    elif func == "relu":
        print(f"ReLU: f({x}) = {relu(x)}")
    else:
        print(f"ELU: f({x}) = {elu(x)}")


#EXERCISE 3


def mae(pred, tar):
    return abs(tar - pred)


def mse(pred, tar):
    return (tar-pred)**2


def exercise3():
    n = input("Input number of samples ( integer number ) which are generated : ")
    if not n.isnumeric():
        print("number of samples must be an integer number")
        return
    loss = input("Input loss name: ").lower()
    if loss == "mae":
        loss_total = 0
        for i in range(int(n)):
            predict = uniform(0, 10)
            target = uniform(0, 10)
            loss_value = mae(predict, target)
            print(f"loss name: MAE, sample: {i}, predict: {predict}, target: {target}, loss: {loss_value}")
            loss_total += loss_value
        print(f"final MAE: {(1/int(n))*loss_total}")
        return
    elif loss == "mse":
        loss_total = 0
        for i in range(int(n)):
            predict = uniform(0, 10)
            target = uniform(0, 10)
            loss_value = mse(predict, target)
            print(f"loss name: MSE, sample: {i}, predict: {predict}, target: {target}, loss: {loss_value}")
            loss_total += loss_value
        print(f"final MSE: {(1 / int(n)) * loss_total}")
        return
    elif loss == "rmse":
        loss_total = 0
        for i in range(int(n)):
            predict = uniform(0, 10)
            target = uniform(0, 10)
            loss_value = mse(predict, target)
            print(f"loss name: RMSE, sample: {i}, predict: {predict}, target: {target}, loss: {loss_value}")
            loss_total += loss_value
        print(f"final RMSE: {sqrt((1 / int(n)) * loss_total)}")
        return
    else:
        print(f"{loss} if not supported")


#EXERCISE 4


def giai_thua(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result


def approx_sin(x, n):
    result = 0
    for i in range(n):
        result += ((-1) ** i) * (x ** (2*i + 1) / giai_thua(2 * i + 1))
    print(result)


def approx_cos(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i) / giai_thua(2*i))
    print(result)


def approx_sinh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2*i + 1)) / giai_thua(2*i + 1)
    print(result)


def approx_cosh(x, n):
    result = 0
    for i in range(n):
        result += (x ** (2 * i)) / giai_thua(2 * i)
    print(result)

#EXERCISE 5


def md_nre_single_sample(y, y_hat, n, p):
    print((y**(1/n)-y_hat**(1/n))**p)
