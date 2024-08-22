import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.combinations_with_replacement")

# Define a list of elements
lst = ['a', 'b', 'c', 'd']

# Generate all possible combinations with replacement of length 2
h = itertools.combinations_with_replacement(lst, 2)
print(type(h))  # Output: <class 'itertools.combinations_with_replacement'>

# Iterate through the combinations and print each
for v in itertools.combinations_with_replacement(lst, 2):
    print(v)
# Output:
# ('a', 'a')
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'b')
# ('b', 'c')
# ('b', 'd')
# ('c', 'c')
# ('c', 'd')
# ('d', 'd')

banner("Example 2: Converting Combinations with Replacement to a List")

# Convert the combinations to a list
h_list = list(itertools.combinations_with_replacement(lst, 2))
print(h_list)
# Output: [('a', 'a'), ('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'b'), ('b', 'c'), ('b', 'd'), ('c', 'c'), ('c', 'd'), ('d', 'd')]

# Print the number of combinations
print(len(h_list))  # Output: 10

banner("Example 3: Generating Combinations with Replacement of Different Lengths")

# Generate all possible combinations with replacement of length 3
h_list_3 = list(itertools.combinations_with_replacement(lst, 3))
print(h_list_3)
# Output: [('a', 'a', 'a'), ('a', 'a', 'b'), ('a', 'a', 'c'), ('a', 'a', 'd'), ('a', 'b', 'b'), ('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'c'), ('a', 'c', 'd'), ('a', 'd', 'd'), ('b', 'b', 'b'), ('b', 'b', 'c'), ('b', 'b', 'd'), ('b', 'c', 'c'), ('b', 'c', 'd'), ('b', 'd', 'd'), ('c', 'c', 'c'), ('c', 'c', 'd'), ('c', 'd', 'd'), ('d', 'd', 'd')]

print(len(h_list_3))  # Output: 20

banner("Example 4: Combinations with Replacement Using Different Data Types")

# Generate combinations with replacement of a mixed list
mixed_list = [1, 'A', 2.5, 'B']
h_mixed = list(itertools.combinations_with_replacement(mixed_list, 2))
print(h_mixed)
# Output: [(1, 1), (1, 'A'), (1, 2.5), (1, 'B'), ('A', 'A'), ('A', 2.5), ('A', 'B'), (2.5, 2.5), (2.5, 'B'), ('B', 'B')]

print(len(h_mixed))  # Output: 10

banner("Example 5: Combinations with Replacement of a String")

# Generate combinations with replacement of a string
STRING = 'ABC'
h_string = list(itertools.combinations_with_replacement(STRING, 2))
print(h_string)
# Output: [('A', 'A'), ('A', 'B'), ('A', 'C'), ('B', 'B'), ('B', 'C'), ('C', 'C')]

print(len(h_string))  # Output: 6

banner("Example 6: Combinations with Replacement of Multiple Iterables")

# Combine two lists and generate combinations with replacement
lst1 = ['1', '2']
lst2 = ['A', 'B']
combined_list = lst1 + lst2

h_combined = list(itertools.combinations_with_replacement(combined_list, 2))
print(h_combined)
# Output: [('1', '1'), ('1', '2'), ('1', 'A'), ('1', 'B'), ('2', '2'), ('2', 'A'), ('2', 'B'), ('A', 'A'), ('A', 'B'), ('B', 'B')]

print(len(h_combined))  # Output: 10

banner("Example 7: Combinations with Replacement Using Numbers")

# Generate combinations with replacement using a list of numbers
numbers = [1, 2, 3]
h_numbers = list(itertools.combinations_with_replacement(numbers, 2))
print(h_numbers)
# Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

print(len(h_numbers))  # Output: 6
