import itertools

def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.permutations with Length 2")

lst = ['a', 'b', 'c', 'd']

p = itertools.permutations(lst, 2)
print(type(p))

for v in itertools.permutations(lst, 2):
    print(v)

p_list = list(itertools.permutations(lst, 2))
print(p_list)

print(len(p_list))

banner("Example 2: Generating All Permutations")

for v in itertools.permutations(lst):
    print(v)

print(len(list(itertools.permutations(lst))))

banner("Example 3: Permutations with Duplicates")

lst = ['a', 'a']

for v in itertools.permutations(lst, 2):
    print(v)

banner("Example 4: Permutations of List with More Elements")

lst = ['a', 'b', 'c', 'd']

for v in itertools.permutations(lst):
    print(v)
