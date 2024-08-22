import itertools

def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.combinations")

lst = ['a', 'b', 'c', 'd']
c = itertools.combinations(lst, 2)
print(type(c))

for v in itertools.combinations(lst, 2):
    print(v)

banner("Example 2: Converting Combinations to a List")

c_list = list(itertools.combinations(lst, 2))
print(c_list)
print(len(c_list))

banner("Example 3: Generating Combinations of Different Lengths")

combinations_length_3 = list(itertools.combinations(lst, 3))
print(combinations_length_3)
print(len(combinations_length_3))

banner("Example 4: Combinations with Repeated Elements")

lst_repeated = ['a', 'a', 'b', 'b']
combinations_repeated = list(itertools.combinations(lst_repeated, 2))
print(combinations_repeated)
print(len(combinations_repeated))

banner("Example 5: Combining Multiple Iterables")

lst1 = ['1', '2', '3']
lst2 = ['A', 'B', 'C']
combinations_multiple_lists = list(itertools.combinations(lst1 + lst2, 2))
print(combinations_multiple_lists)
print(len(combinations_multiple_lists))

banner("Example 6: Using itertools.combinations with a String")

STRING = 'ABCD'
combinations_string = list(itertools.combinations(STRING, 3))
print(combinations_string)
print(len(combinations_string))

banner("Example 7: Combinations with Different Data Types")

lst_mixed = [1, 'A', 2.5, 'B']
combinations_mixed = list(itertools.combinations(lst_mixed, 2))
print(combinations_mixed)
print(len(combinations_mixed))
