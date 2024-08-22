import itertools

def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

print()
banner("Example 1: Count Method, No Arguments")
for i in itertools.count():
    print(i)
    if i > 5:
        break

banner("Example 2: Count Method, With Start Argument")
for i in itertools.count(2):
    print(i)
    if i > 3:
        break

banner("Example 3: Count Method, With Step Argument")
for i in itertools.count(step=3):
    print(i)
    if i > 8:
        break

banner("Example 4: Count Method, With Start and Step Arguments")
for i in itertools.count(2, 3):
    print(i)
    if i > 8:
        break

banner("Example 5: Count Method, With Negative Step")
for i in itertools.count(10, -1):
    print(i)
    if i < 8:
        break

banner("Example 6: Count Method, With Floating-Point Step")
for i in itertools.count(0.1, 1.5):
    print(i)
    if i > 3:
        break

banner("Example 7: Generating a Sequence Using count() and Calculated Values")
for i in itertools.count():
    calculated_value = 0.1 + 1.5 * i
    print(calculated_value)
    if calculated_value > 3:
        break

banner("Example 8: count() with zip to Pair Elements with Indices")
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

indexed_pairs = list(zip(itertools.count(), l1, l2))
print(indexed_pairs)

banner("Example 9: Using enumerate() with zip()")
enumerated_pairs = list(enumerate(zip(l1, l2)))
print(enumerated_pairs)

banner("Example 10: Infinite Iteration with cycle()")
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    counter += 1
    if counter > 6:
        break