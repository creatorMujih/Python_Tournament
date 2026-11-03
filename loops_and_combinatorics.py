#without itertools

names = ['A', 'B', 'C', 'D']

pairs = []

for i in range(len(names)):
    for j in range(i + 1, len(names)):
        pairs.append((names[i], names[j]))

print(pairs)
print("Total pairs:", len(pairs))


#with itertools

from itertools import combinations

names = ['A', 'B', 'C', 'D']

pairs = list(combinations(names, 2))

print(pairs)
print("Total pairs:", len(pairs))

