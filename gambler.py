
from collections import defaultdict
import random
import math

scores_for_max = [1, 1, 6, 15, 28]
def get_score(cards):
    counts = defaultdict(int)
    for card in cards:
        counts[card] += 1
    score = 0
    score -= 2 * counts[11]
    del counts[11]
    # score += 2**max(counts.values() + [0]) - 1
    # score += 2**max(counts.values() + [0])
    score += scores_for_max[max(counts.values() + [0])]
    return score

nrounds = 1000000
total = 0
hist = defaultdict(int)
all_cards = [i for i in range(52) if i != 11]
for _ in range(nrounds):
    # cards = random.sample(range(52), 4)
    cards = [(i - 1) % 13 + 1 for i in random.sample(all_cards, 4)]
    score = get_score(cards)
    # print 'counts', counts, score

    total += score
    hist[score] += 1
print 'total', total
print 'histogram', hist
print 'average', ((0.0 + total) / nrounds)
