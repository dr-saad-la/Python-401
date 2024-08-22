import itertools

def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.groupby with a List")

l = [0, 0, 0, 1, 1, 2, 0, 0]
print([(k, list(g)) for k, g in itertools.groupby(l)])

print(itertools.groupby(l))

for k, g in itertools.groupby(l):
    print(k, g)

for k, g in itertools.groupby(l):
    print(k, list(g))

print([k for k, g in itertools.groupby(l)])

print([list(g) for k, g in itertools.groupby(l)])

print([(k, list(g)) for k, g in itertools.groupby(l)])

banner("Example 2: Grouping by Length of Strings")

l = ['aaa', 'bbb', 'ccc', 'a', 'b', 'aa', 'bb']
print([(k, list(g)) for k, g in itertools.groupby(l, len)])

banner("Example 3: Grouping by Even/Odd Numbers")

l = [0, 2, 0, 3, 1, 4, 4, 0]
print([(k, list(g)) for k, g in itertools.groupby(l, lambda x: x % 2)])

banner("Example 4: Grouping by a Specific Key in a Nested List")

l = [[0, 'Alice', 0],
     [1, 'Alice', 10],
     [2, 'Bob', 20],
     [3, 'Bob', 30],
     [4, 'Alice', 40]]

for k, g in itertools.groupby(l, lambda x: x[1]):
    print(k, list(g))

banner("Example 5: Grouping after Sorting by Key")

for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, list(g))

for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, sum(x[2] for x in g))

banner("Example 6: Grouping with Tuples")

t = (0, 0, 0, 1, 1, 2, 0, 0)
print([(k, list(g)) for k, g in itertools.groupby(t)])

print(tuple((k, tuple(g)) for k, g in itertools.groupby(t)))

banner("Example 7: Grouping Characters in a String")

S = 'aaabbcaa'
print([(k, list(g)) for k, g in itertools.groupby(S)])

print([(k, ''.join(g)) for k, g in itertools.groupby(S)])
