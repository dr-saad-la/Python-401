import itertools
import pprint

def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

banner("Example 1: Basic Usage of itertools.product")

l1 = [1, 2, 3]
l2 = ['A', 'B']

product_result = itertools.product(l1, l2)
print(product_result)

print(type(product_result))

for v in product_result:
    print(v)

product_result = itertools.product(l1, l2)

for v1, v2 in product_result:
    print(v1, v2)

for v1 in l1:
    for v2 in l2:
        print(v1, v2)

banner("Example 2: Converting itertools.product to a List")

l1 = [1, 2, 3]
l2 = ['A', 'B']
l_p = list(itertools.product(l1, l2))
print(l_p)

print(type(l_p))

print(type(l_p[0]))

banner("Example 3: Cartesian Product with Multiple Iterables")

t = ('A', 'B')
d = {'key1': 'value1', 'key2': 'value2'}
r = range(2)

pprint.pprint(list(itertools.product(t, d, r)))

banner("Example 4: Using 'repeat' Argument in itertools.product")

l1 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, repeat=3)))

pprint.pprint(list(itertools.product(l1, l1, l1)))

banner("Example 5: Complex Cartesian Product")

l1 = [1, 2]
l2 = ['A', 'B']

pprint.pprint(list(itertools.product(l1, l2, repeat=2)))

pprint.pprint(list(itertools.product(l1, l2, l1, l2)))
