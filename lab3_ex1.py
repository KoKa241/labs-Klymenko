import math
from random import randint

def gauss_func(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coefficient * math.exp(exponent)

for i in range(5):
    x = randint(0, 1000)
    mu = randint(0, 500)
    sigma = randint(0, 100)
    print(gauss_func(x, mu, sigma))
