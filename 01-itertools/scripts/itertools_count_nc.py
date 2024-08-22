"""
This module demonstrates the use of itertools.count() and itertools.cycle() through various examples.
"""

import itertools

def banner(title, sep="*", nchar=72):
    """
    Print a banner with a title centered, surrounded by a separator character.
    
    Args:
        title (str): The title to display.
        sep (str): The separator character.
        nchar (int): The number of characters for the banner width.
    """
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

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
list_1 = ['a', 'b', 'c']
list_2 = ['x', 'y', 'z']

indexed_pairs = list(zip(itertools.count(), list_1, list_2))
print(indexed_pairs)

banner("Example 9: Using enumerate() with zip()")
enumerated_pairs = list(enumerate(zip(list_1, list_2)))
print(enumerated_pairs)

banner("Example 10: Infinite Iteration with cycle()")
COUNTER = 0
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    COUNTER += 1
    if COUNTER > 6:
        break
        