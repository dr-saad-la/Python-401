import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

# Generate all possible permutations of a list
banner("Example 1: Basic Usage of itertools.permutations with Length 2")

lst = ['a', 'b', 'c', 'd']

# Generate permutations of length 2
p = itertools.permutations(lst, 2)
print(type(p))
# Output: <class 'itertools.permutations'>

# Iterate through permutations and print each one
for v in itertools.permutations(lst, 2):
    print(v)
# Output:
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'a')
# ('b', 'c')
# ('b', 'd')
# ('c', 'a')
# ('c', 'b')
# ('c', 'd')
# ('d', 'a')
# ('d', 'b')
# ('d', 'c')

# Convert permutations to a list and print
p_list = list(itertools.permutations(lst, 2))
print(p_list)
# Output: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'a'), ('b', 'c'), ('b', 'd'),
#          ('c', 'a'), ('c', 'b'), ('c', 'd'), ('d', 'a'), ('d', 'b'), ('d', 'c')]

# Print the length of the permutations list
print(len(p_list))
# Output: 12

# Generate all possible permutations of the list without specifying length
banner("Example 2: Generating All Permutations")

for v in itertools.permutations(lst):
    print(v)
# Output:
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')

# Print the total number of permutations
print(len(list(itertools.permutations(lst))))
# Output: 24

# Handling a list with duplicate elements
banner("Example 3: Permutations with Duplicates")

lst = ['a', 'a']

for v in itertools.permutations(lst, 2):
    print(v)
# Output:
# ('a', 'a')
# ('a', 'a')

banner("Example 4: Permutations of List with More Elements")

lst = ['a', 'b', 'c', 'd']

# Generate and print all permutations
for v in itertools.permutations(lst):
    print(v)

# Output:
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')
