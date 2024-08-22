import itertools
import operator


def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)


# Introduction to itertools.accumulate()
# The itertools.accumulate() function makes an iterator that returns accumulated sums or the result
# of other binary functions (specified via the func parameter). It's similar to functools.reduce(),
# but it returns the intermediate results as well.

banner("Example 1: Using accumulate() for Summation")

# Define a list of integers
lst = [1, 2, 3, 4, 5, 6]

# Using accumulate to sum the elements of the list
# It returns cumulative sums by default
accum_result = itertools.accumulate(lst)
print(list(accum_result))
# Output: [1, 3, 6, 10, 15, 21]

banner("Example 2: Using accumulate() with Multiplication")

# Using accumulate with operator.mul to get cumulative products
accum_result = itertools.accumulate(lst, func=operator.mul)
print(list(accum_result))
# Output: [1, 2, 6, 24, 120, 720]

banner("Example 3: Using accumulate() with Subtraction")

# Using accumulate with operator.sub to get cumulative differences
accum_result = itertools.accumulate(lst, func=operator.sub)
print(list(accum_result))
# Output: [1, -1, -4, -8, -13, -19]

banner("Example 4: Using accumulate() with Division")

# Using accumulate with operator.truediv to get cumulative division results
accum_result = itertools.accumulate(lst, func=operator.truediv)
print(list(accum_result))
# Output: [1, 0.5, 0.16666666666666666, 0.041666666666666664, 0.008333333333333333, 0.001388888888888889]

banner("Example 5: Using accumulate() with max Function")

# Using accumulate with max function to get cumulative maximum values
accum_result = itertools.accumulate([1, 3, 2, 6, 5, 4], func=max)
print(list(accum_result))
# Output: [1, 3, 3, 6, 6, 6]

banner("Example 6: Using accumulate() with a Lambda Function")

# Using accumulate with a lambda function to multiply elements
accum_result = itertools.accumulate(lst, func=lambda x, y: x * y)
print(list(accum_result))
# Output: [1, 2, 6, 24, 120, 720]

banner("Example 7: Using accumulate() with String Concatenation")

# Using accumulate with a lambda function to concatenate integers as strings
accum_result = itertools.accumulate(lst, func=lambda x, y: int(str(x) + str(y)))
print(list(accum_result))
# Output: [1, 12, 123, 1234, 12345, 123456]

banner("Example 8: Using accumulate() with Reverse Order")

# Using accumulate with a reversed list
accum_result = itertools.accumulate(reversed(lst))
print(list(accum_result))
# Output: [6, 11, 15, 18, 20, 21]

banner("Example 9: Using accumulate() with Initial Value")

# Using accumulate with an initial value
accum_result = itertools.accumulate(lst, initial=100)
print(list(accum_result))
# Output: [100, 101, 103, 106, 110, 115, 121]

banner("Example 10: Using accumulate() with Initial Value 0")

# Using accumulate with an initial value of 0
accum_result = itertools.accumulate(lst, initial=0)
print(list(accum_result))
# Output: [0, 1, 3, 6, 10, 15, 21]