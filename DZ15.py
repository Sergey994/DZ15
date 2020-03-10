from random import randint


def list_generator():
    res = []
    for i in range(1, randint(50)):
        res.append(randint(-100, 100))

    return res
