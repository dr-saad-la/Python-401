import itertools

def banner(title, sep="*", nchar=72):
    """Print a banner with a title centered, surrounded by a separator character."""
    print(sep * nchar)
    print(title.center(nchar))
    print(sep * nchar)

# Introduction to itertools.cycle()
# The itertools.cycle() function creates an iterator that returns elements from the iterable indefinitely.
# Once all elements have been returned, it starts again from the beginning.
# It's useful for repeating a sequence of values, like in a round-robin scenario.

print()
banner("Example 1: Using cycle() to Repeat a List Indefinitely")

# Define a list with three elements
l = [1, 10, 100]

# Initialize a variable to sum the values from the cycle
SUM_VALUE = 0

# Use cycle() to iterate over the list indefinitely
for i in itertools.cycle(l):
    print(i)
    SUM_VALUE += i  # Add the current value to the sum
    if SUM_VALUE > 300:  # Stop the loop when the sum exceeds 300
        break

banner("Example 2: Using cycle() with a Range of Numbers")

# Use cycle() with a range object to repeat a sequence of numbers
SUM_VALUE = 0

for i in itertools.cycle(range(3)):  # cycle through 0, 1, 2 repeatedly
    print(i)
    SUM_VALUE += i  # Add the current value to the sum
    if SUM_VALUE > 5:  # Stop the loop when the sum exceeds 5
        break


banner("Example 3: Combining cycle() with zip() for Repeating Patterns")

# Define two lists of different lengths
lst_1 = [1, 10, 100]
lst_2 = [0, 1, 2, 3, 4, 5, 6]

# Use cycle() to repeat the elements of lst_1 until lst_2 is exhausted
# zip() pairs elements from both lists together
print(list(zip(itertools.cycle(lst_1), lst_2)))


# itertools.cycle() allows you to seamlessly handle cases where one list is shorter than another,
# ensuring that the shorter list's elements are cycled through to match the length of the longer list.

banner("Example 4: Infinite Iteration with cycle()")

# Another practical use of cycle() is to create an infinite loop of characters or actions.
# In this example, we simulate a repetitive task using cycle().

COUNTER = 0  # Initialize a counter to limit the loop

# Use cycle() to indefinitely loop through the sequence ['A', 'B', 'C']
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    COUNTER += 1
    if COUNTER > 6:  # Stop after 7 iterations
        break

banner("Example 5: Cycling Through Multiple Iterables")

# cycle() can also be used with multiple iterables by combining it with itertools.chain()
# This can be useful when you need to cycle through multiple lists or sequences

lst_3 = ['red', 'green', 'blue']
lst_4 = ['circle', 'square', 'triangle']

# Chain the two lists together and cycle through the combined sequence
cycled_shapes = itertools.cycle(itertools.chain(lst_3, lst_4))

# Display the first 10 items in the cycled sequence
for _ in range(10):
    print(next(cycled_shapes))


banner("Example 6: Cycling Through a Pattern of Actions")

# Simulate a repetitive pattern of actions using cycle()
# For example, cycling through a sequence of operations in a game or process

actions = ['move', 'jump', 'crouch']

# Cycle through the actions indefinitely
cycled_actions = itertools.cycle(actions)

# Simulate performing these actions for a specific number of steps
for step in range(7):
    action = next(cycled_actions)
    print(f"Step {step + 1}: {action}")


banner("Example 7: Cycling Through an Infinite Pattern with Conditional Exit")

# Another scenario could be a system where an action is repeated until a condition is met.
# Here, we simulate a traffic light system that cycles through colors until a certain condition is met.

traffic_lights = ['green', 'yellow', 'red']
light_cycle = itertools.cycle(traffic_lights)

# Simulate the traffic light system until it turns red twice
RED_COUNT = 0

while RED_COUNT < 2:
    current_light = next(light_cycle)
    print(current_light)
    if current_light == 'red':
        RED_COUNT += 1


# The loop exits after the red light appears twice.
