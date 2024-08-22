import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.combinations")

# Define a list of elements
lst = ['a', 'b', 'c', 'd']

# Create an itertools.combinations object to generate all possible combinations of length 2
c = itertools.combinations(lst, 2)

# Display the type of the combinations object
print(type(c))
# Output: <class 'itertools.combinations'>

# Iterate through the combinations and print each pair
for v in itertools.combinations(lst, 2):
    print(v)
# Output:
# ('a', 'b')
# ('a', 'c')
# ('a', 'd')
# ('b', 'c')
# ('b', 'd')
# ('c', 'd')

banner("Example 2: Converting Combinations to a List")

# Convert the combinations object to a list for easier manipulation and display
c_list = list(itertools.combinations(lst, 2))
print(c_list)
# Output: [('a', 'b'), ('a', 'c'), ('a', 'd'), ('b', 'c'), ('b', 'd'), ('c', 'd')]

# Display the number of combinations generated
print(len(c_list))
# Output: 6

banner("Example 3: Generating Combinations of Different Lengths")

# Generate all combinations of length 3 from the list
combinations_length_3 = list(itertools.combinations(lst, 3))
print(combinations_length_3)
# Output: [('a', 'b', 'c'), ('a', 'b', 'd'), ('a', 'c', 'd'), ('b', 'c', 'd')]

# Display the number of combinations generated
print(len(combinations_length_3))
# Output: 4

banner("Example 4: Combinations with Repeated Elements")

# Define a list with repeated elements
lst_repeated = ['a', 'a', 'b', 'b']

# Generate combinations of length 2
combinations_repeated = list(itertools.combinations(lst_repeated, 2))
print(combinations_repeated)
# Output: [('a', 'a'), ('a', 'b'), ('a', 'b'), ('a', 'b'), ('a', 'b'), ('b', 'b')]

# Display the number of combinations generated
print(len(combinations_repeated))
# Output: 6

banner("Example 5: Combining Multiple Iterables")

# Define two different lists
lst1 = ['1', '2', '3']
lst2 = ['A', 'B', 'C']

# Generate combinations by combining elements from both lists
combinations_multiple_lists = list(itertools.combinations(lst1 + lst2, 2))
print(combinations_multiple_lists)
# Output: [('1', '2'), ('1', '3'), ('1', 'A'), ('1', 'B'), ('1', 'C'),
#          ('2', '3'), ('2', 'A'), ('2', 'B'), ('2', 'C'),
#          ('3', 'A'), ('3', 'B'), ('3', 'C'),
#          ('A', 'B'), ('A', 'C'), ('B', 'C')]

# Display the number of combinations generated
print(len(combinations_multiple_lists))
# Output: 15

banner("Example 6: Using itertools.combinations with a String")

# Generate combinations of characters from a string
STRING = 'ABCD'
combinations_string = list(itertools.combinations(STRING, 3))
print(combinations_string)
# Output: [('A', 'B', 'C'), ('A', 'B', 'D'), ('A', 'C', 'D'), ('B', 'C', 'D')]

# Display the number of combinations generated
print(len(combinations_string))
# Output: 4

banner("Example 7: Combinations with Different Data Types")

# Define a list with different data types
lst_mixed = [1, 'A', 2.5, 'B']

# Generate combinations of length 2
combinations_mixed = list(itertools.combinations(lst_mixed, 2))
print(combinations_mixed)
# Output: [(1, 'A'), (1, 2.5), (1, 'B'), ('A', 2.5), ('A', 'B'), (2.5, 'B')]

# Display the number of combinations generated
print(len(combinations_mixed))
# Output: 6
