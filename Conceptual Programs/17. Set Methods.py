val = {"hello", "Steel", 11, 13}
if 13 in val:
    print(True)
else:
    print(False)

# val.clear()
print(val)

a = val.pop()
print(f"the value popped is {a}")
print(val)

# The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.