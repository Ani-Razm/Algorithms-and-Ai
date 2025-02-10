from itertools import permutations

p = list(permutations(["a", "b", "c", "d"]))

counter = 0
for per in p:
    print(">".join(per))
    counter += 1

print(counter)