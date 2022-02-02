import random
from collections import defaultdict

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element


pick_list = [random.randint(0, 10000000) for i in range(0, 1000)]
results = defaultdict(int)
for i in range(100000):
    random_pick = pick(pick_list)
    results[pick_list.index(random_pick)] += 1