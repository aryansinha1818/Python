l1 = ("man","chair", "tree", 'pen', "eraser")
for q in enumerate(l1):
    print(q)
for i, p in enumerate(l1):
    print(i,p)


# What these code would do
# for l1 in enumerate(l1):
#     print(l1)
# for i, l1 in enumerate(l1):
#     print(i,l1)
"""(0, 'man')
(1, 'chair')
(2, 'tree')
(3, 'pen')
(4, 'eraser')
After this loop, l1 is now a tuple containing the last index-value pair (4, 'eraser').

Second Loop:

python
Copy code
for i, l1 in enumerate(l1):
    print(i, l1)
Now, l1 is the tuple (4, 'eraser') from the previous loop. When enumerate is called on this, it treats it as a two-element tuple.

In the first iteration, i will be 0 and l1 will be 4.
In the second iteration, i will be 1 and l1 will be 'eraser'
l1 = ("man","chair", "tree", 'pen', "eraser")"""

