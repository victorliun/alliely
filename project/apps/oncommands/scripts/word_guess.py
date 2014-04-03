import enchant
from datetime import datetime
from itertools import permutations

def time_dec(func):
    def f_wrap(*args, **kwargs):
        start = datetime.now()
        res =func(*args, **kwargs)
        end = datetime.now()

        duration = end - start
        print "Excute %s takes %s." %(func.__name__, duration)
        return res
    return f_wrap

@time_dec
def word_guess(letters, length=None):
    """ give the possible word from the letters at a certon length"""
    length  = length or len(letters)
    #letters = [ ch for ch in letters]
    results = []
    en_dict = enchant.Dict("en_US")

    for word in permutations(letters, length):
        #word  = ''.join(word)
        if en_dict.check(word):
            results.append(word)

    res = set(results)

    return res

