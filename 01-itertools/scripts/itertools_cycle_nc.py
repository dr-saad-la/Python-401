"""
This module demonstrates the use of itertools.cycle() through various examples.
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

banner("Example 1: Using cycle() to Repeat a List Indefinitely")

l = [1, 10, 100]
sum_value = 0

for i in itertools.cycle(l):
    print(i)
    sum_value += i
    if sum_value > 300:
        break

banner("Example 2: Using cycle() with a Range of Numbers")

sum_value = 0

for i in itertools.cycle(range(3)):
    print(i)
    sum_value += i
    if sum_value > 5:
        break

banner("Example 3: Combining cycle() with zip() for Repeating Patterns")

lst_1 = [1, 10, 100]
lst_2 = [0, 1, 2, 3, 4, 5, 6]

print(list(zip(itertools.cycle(lst_1), lst_2)))

banner("Example 4: Infinite Iteration with cycle()")

counter = 0

for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    counter += 1
    if counter > 6:
        break

banner("Example 5: Cycling Through Multiple Iterables")

lst_3 = ['red', 'green', 'blue']
lst_4 = ['circle', 'square', 'triangle']

cycled_shapes = itertools.cycle(itertools.chain(lst_3, lst_4))

for _ in range(10):
    print(next(cycled_shapes))

banner("Example 6: Cycling Through a Pattern of Actions")

actions = ['move', 'jump', 'crouch']
cycled_actions = itertools.cycle(actions)

for step in range(7):
    action = next(cycled_actions)
    print(f"Step {step + 1}: {action}")

banner("Example 7: Cycling Through an Infinite Pattern with Conditional Exit")

traffic_lights = ['green', 'yellow', 'red']
red_count = 0
light_cycle = itertools.cycle(traffic_lights)

while red_count < 2:
    current_light = next(light_cycle)
    print(current_light)
    if current_light == 'red':
        red_count += 1