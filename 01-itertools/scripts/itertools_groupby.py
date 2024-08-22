import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

# Group elements in a list using itertools.groupby
banner("Example 1: Basic Usage of itertools.groupby with a List")

l = [0, 0, 0, 1, 1, 2, 0, 0]
# Group elements and print the groups
print([(k, list(g)) for k, g in itertools.groupby(l)])
# Output: [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

# Check the type of the groupby object
print(itertools.groupby(l))
# Output: <itertools.groupby object at 0x...>

# Iterate through the groups and print the group key and the group object
for k, g in itertools.groupby(l):
    print(k, g)
# Output:
# 0 <itertools._grouper object at 0x...>
# 1 <itertools._grouper object at 0x...>
# 2 <itertools._grouper object at 0x...>
# 0 <itertools._grouper object at 0x...>

# Convert each group object to a list and print it
for k, g in itertools.groupby(l):
    print(k, list(g))
# Output:
# 0 [0, 0, 0]
# 1 [1, 1]
# 2 [2]
# 0 [0, 0]

# Print just the keys from the grouped list
print([k for k, g in itertools.groupby(l)])
# Output: [0, 1, 2, 0]

# Print just the groups (as lists) from the grouped list
print([list(g) for k, g in itertools.groupby(l)])
# Output: [[0, 0, 0], [1, 1], [2], [0, 0]]

# Print both the keys and their corresponding groups
print([(k, list(g)) for k, g in itertools.groupby(l)])
# Output: [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

# Group strings by their length
banner("Example 2: Grouping by Length of Strings")

l = ['aaa', 'bbb', 'ccc', 'a', 'b', 'aa', 'bb']
print([(k, list(g)) for k, g in itertools.groupby(l, len)])
# Output: [(3, ['aaa', 'bbb', 'ccc']), (1, ['a', 'b']), (2, ['aa', 'bb'])]

# Group numbers by even and odd values using a lambda function
banner("Example 3: Grouping by Even/Odd Numbers")

l = [0, 2, 0, 3, 1, 4, 4, 0]
print([(k, list(g)) for k, g in itertools.groupby(l, lambda x: x % 2)])
# Output: [(0, [0, 2, 0]), (1, [3, 1]), (0, [4, 4, 0])]

# Group nested lists by the second element
banner("Example 4: Grouping by a Specific Key in a Nested List")

l = [[0, 'Alice', 0],
     [1, 'Alice', 10],
     [2, 'Bob', 20],
     [3, 'Bob', 30],
     [4, 'Alice', 40]]

for k, g in itertools.groupby(l, lambda x: x[1]):
    print(k, list(g))
# Output:
# Alice [[0, 'Alice', 0], [1, 'Alice', 10]]
# Bob [[2, 'Bob', 20], [3, 'Bob', 30]]
# Alice [[4, 'Alice', 40]]

# Sort the list by the second element and group them
banner("Example 5: Grouping after Sorting by Key")

for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, list(g))
# Output:
# Alice [[0, 'Alice', 0], [1, 'Alice', 10], [4, 'Alice', 40]]
# Bob [[2, 'Bob', 20], [3, 'Bob', 30]]

# Sum the third elements grouped by the second element after sorting
for k, g in itertools.groupby(sorted(l, key=lambda x: x[1]), lambda x: x[1]):
    print(k, sum(x[2] for x in g))
# Output:
# Alice 50
# Bob 50

# Group elements in a tuple
banner("Example 6: Grouping with Tuples")

t = (0, 0, 0, 1, 1, 2, 0, 0)
print([(k, list(g)) for k, g in itertools.groupby(t)])
# Output: [(0, [0, 0, 0]), (1, [1, 1]), (2, [2]), (0, [0, 0])]

print(tuple((k, tuple(g)) for k, g in itertools.groupby(t)))
# Output: ((0, (0, 0, 0)), (1, (1, 1)), (2, (2,)), (0, (0, 0)))

# Group characters in a string
banner("Example 7: Grouping Characters in a String")

S = 'aaabbcaa'
print([(k, list(g)) for k, g in itertools.groupby(S)])
# Output: [('a', ['a', 'a', 'a']), ('b', ['b', 'b']), ('c', ['c']), ('a', ['a', 'a'])]

print([(k, ''.join(g)) for k, g in itertools.groupby(S)])
# Output: [('a', 'aaa'), ('b', 'bb'), ('c', 'c'), ('a', 'aa')]
