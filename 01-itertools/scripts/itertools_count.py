# import itertools module
import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

# The itertools.count() function generates an infinite sequence of numbers.
# This sequence starts at the specified start value and increments by the step value (default is 1).
# It is particularly useful when you need a constant stream of incrementing numbers.
# Note: Since it's infinite, always use a condition to break the loop.

print()
banner("Example 1: Count Method, No Arguments")
# No arguments: Starts at 0 and increments by 1
for i in itertools.count():
    print(i)
    if i > 5:  # Break the loop after 6 iterations to prevent infinite output
        break

banner("Example 2: Count Method, With Start Argument")
# Starts counting from 2 and increments by 1
for i in itertools.count(2):
    print(i)
    if i > 3:  # Break after 2 iterations
        break

banner("Example 3: Count Method, With Step Argument")
# Starts at 0 and increments by 3
for i in itertools.count(step=3):
    print(i)
    if i > 8:  # Break after the third step
        break

banner("Example 4: Count Method, With Start and Step Arguments")
# Starts at 2 and increments by 3
for i in itertools.count(2, 3):
    print(i)
    if i > 8:  # Break after the second step
        break

banner("Example 5: Count Method, With Negative Step")
# Starts at 10 and decrements by 1
for i in itertools.count(10, -1):
    print(i)
    if i < 8:  # Break when the value drops below 8
        break

banner("Example 6: Count Method, With Floating-Point Step")
# Starts at 0.1 and increments by 1.5 (floating-point numbers)
for i in itertools.count(0.1, 1.5):
    print(i)
    if i > 3:  # Break after a few iterations
        break

banner("Example 7: Generating a Sequence Using count() and Calculated Values")
# Using count to generate a custom sequence
for i in itertools.count():
    calculated_value = 0.1 + 1.5 * i  # Custom calculation
    print(calculated_value)
    if calculated_value > 3:  # Break when the calculated value exceeds 3
        break

banner("Example 8: count() with zip to Pair Elements with Indices")
# Use count() with zip to enumerate elements from two lists
# This pairs each element in l1 and l2 with a corresponding index.
l1 = ['a', 'b', 'c']
l2 = ['x', 'y', 'z']

# itertools.count() starts from 0 by default, pairs each index with elements from l1 and l2
indexed_pairs = list(zip(itertools.count(), l1, l2))
print(indexed_pairs)

banner("Example 9: Using enumerate() with zip()")
# Similar to the previous example, but using Python's built-in enumerate
# enumerate() returns both the index and the element from the iterable
enumerated_pairs = list(enumerate(zip(l1, l2)))
print(enumerated_pairs)

# Additional Examples

banner("Example 10: Infinite Iteration with cycle()")
# The itertools.cycle() function repeats the elements of an iterable indefinitely
# Here, we cycle through a short list indefinitely.
counter = 0
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    counter += 1
    if counter > 6:  # Break after 7 iterations
        break