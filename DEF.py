import random


def print_params(a, b):
    params = [1, 3, 4, 6, 7, 8]
    height = random.choice(params)
    params.remove(height)
    width = random.choice(params)
    print(a, b)
    return (height, width)


height, width = print_params('a', 'b')
print(height, width)
