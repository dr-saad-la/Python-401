import itertools
import pprint

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

# itertools.product generates the Cartesian product of input iterables.
banner("Example 1: Basic Usage of itertools.product")

l1 = [1, 2, 3]
l2 = ['A', 'B']

# Generate the Cartesian product of l1 and l2
product_result = itertools.product(l1, l2)
print(product_result)
# Output: <itertools.product object at 0x...>

print(type(product_result))
# Output: <class 'itertools.product'>

# Iterating through the product
for v in product_result:
    print(v)
# Output:
# (1, 'A')
# (1, 'B')
# (2, 'A')
# (2, 'B')
# (3, 'A')
# (3, 'B')

# Resetting the product result as it is an iterator
product_result = itertools.product(l1, l2)

# Iterate and unpack the result
for v1, v2 in product_result:
    print(v1, v2)
# Output:
# 1 A
# 1 B
# 2 A
# 2 B
# 3 A
# 3 B

# Nested loops achieving the same as itertools.product
for v1 in l1:
    for v2 in l2:
        print(v1, v2)
# Output:
# 1 A
# 1 B
# 2 A
# 2 B
# 3 A
# 3 B

banner("Example 2: Converting itertools.product to a List")

# Converting product to a list
l1 = [1, 2, 3]
l2 = ['A', 'B']
l_p = list(itertools.product(l1, l2))
print(l_p)
# Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B'), (3, 'A'), (3, 'B')]

print(type(l_p))
# Output: <class 'list'>

print(type(l_p[0]))
# Output: <class 'tuple'>

banner("Example 3: Cartesian Product with Multiple Iterables")

t = ('A', 'B')
d = {'key1': 'value1', 'key2': 'value2'}
r = range(2)

# Using itertools.product with multiple iterables
pprint.pprint(list(itertools.product(t, d, r)))
# Output:
# [('A', 'key1', 0),
#  ('A', 'key1', 1),
#  ('A', 'key2', 0),
#  ('A', 'key2', 1),
#  ('B', 'key1', 0),
#  ('B', 'key1', 1),
#  ('B', 'key2', 0),
#  ('B', 'key2', 1)]

banner("Example 4: Using 'repeat' Argument in itertools.product")

# Using repeat to generate the product of an iterable with itself
l1 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, repeat=3)))
# Output:
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

# Equivalent to using multiple iterables
pprint.pprint(list(itertools.product(l1, l1, l1)))
# Output:
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

banner("Example 5: Complex Cartesian Product")

# Cartesian product with two different lists and repeat argument
l1 = [1, 2]
l2 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, l2, repeat=2)))
# Output:
# [(1, 'A', 1, 'A'),
#  (1, 'A', 1, 'B'),
#  (1, 'A', 2, 'A'),
#  (1, 'A', 2, 'B'),
#  (1, 'B', 1, 'A'),
#  (1, 'B', 1, 'B'),
#  (1, 'B', 2, 'A'),
#  (1, 'B', 2, 'B'),
#  (2, 'A', 1, 'A'),
#  (2, 'A', 1, 'B'),
#  (2, 'A', 2, 'A'),
#  (2, 'A', 2, 'B'),
#  (2, 'B', 1, 'A'),
#  (2, 'B', 1, 'B'),
#  (2, 'B', 2, 'A'),
#  (2, 'B', 2, 'B')]

# Cartesian product with four different iterables
pprint.pprint(list(itertools.product(l1, l2, l1, l2)))
# Output:
# [(1, 'A', 1, 'A'),
#  (1, 'A', 1, 'B'),
#  (1, 'A', 2, 'A'),
#  (1, 'A', 2, 'B'),
#  (1, 'B', 1, 'A'),
#  (1, 'B', 1, 'B'),
#  (1, 'B', 2, 'A'),
#  (1, 'B', 2, 'B'),
#  (2, 'A', 1, 'A'),
#  (2, 'A', 1, 'B'),
#  (2, 'A', 2, 'A'),
#  (2, 'A', 2, 'B'),
#  (2, 'B', 1, 'A'),
#  (2, 'B', 1, 'B'),
#  (2, 'B', 2, 'A'),
#  (2, 'B', 2, 'B')]
