import itertools
import operator


def banner(title, sep="*", nchar=72):
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)


banner("Example 1: Using accumulate() for Summation")
lst = [1, 2, 3, 4, 5, 6]
accum_result = itertools.accumulate(lst)
print(list(accum_result))

banner("Example 2: Using accumulate() with Multiplication")
accum_result = itertools.accumulate(lst, func=operator.mul)
print(list(accum_result))

banner("Example 3: Using accumulate() with Subtraction")
accum_result = itertools.accumulate(lst, func=operator.sub)
print(list(accum_result))

banner("Example 4: Using accumulate() with Division")
accum_result = itertools.accumulate(lst, func=operator.truediv)
print(list(accum_result))

banner("Example 5: Using accumulate() with max Function")
accum_result = itertools.accumulate([1, 3, 2, 6, 5, 4], func=max)
print(list(accum_result))

banner("Example 6: Using accumulate() with a Lambda Function")
accum_result = itertools.accumulate(lst, func=lambda x, y: x * y)
print(list(accum_result))

banner("Example 7: Using accumulate() with String Concatenation")
accum_result = itertools.accumulate(lst, func=lambda x, y: int(str(x) + str(y)))
print(list(accum_result))

banner("Example 8: Using accumulate() with Reverse Order")
accum_result = itertools.accumulate(reversed(lst))
print(list(accum_result))

banner("Example 9: Using accumulate() with Initial Value")
accum_result = itertools.accumulate(lst, initial=100)
print(list(accum_result))

banner("Example 10: Using accumulate() with Initial Value 0")
accum_result = itertools.accumulate(lst, initial=0)
print(list(accum_result))
