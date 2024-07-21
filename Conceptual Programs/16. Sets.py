"""
1. {}
2. unique elements
3. set supports mathematical operations like union, intersection, difference.
4. sets can be both mutable and immutable
mutable_set = {1,2,3}
immutable_set = frozenset([1,2,3]) - append and remove won't work here.
5. sets can be beneficiary for removing duplicates from a list
 l1 = [1,2,3,4,5,5]
 uniques_set = list(set(l1))
 print(unique_set)
 l1->set->list
 unique_set = set(l1)
 print(unique_set)
"""


# sq bracket - lists
# () - tuples
# {} - sets
s1 = {"hello", "Aryan", 9.0, 8,100,"a"}
print(s1)
s2 = {}
print(type(s2))
for i in s1:
    print(f"{i} ")
    
s3 = {"world", "Petter", 999.0, 81,1200,"a"}
# return a new set
print(s1.union(s3))
# adds the new value to the existing sets
print(s1.update(s3))
print(s1)

# intersection - returns a new set prints only items that are similar to both the sets
#  intersection_update - existing set would get updated

# The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets. The symmetric_difference() method returns a new set whereas symmetric_difference_update() method updates into the existing set from another set



"""
# list 
1. when we want to sort collections
2. maintain the order
3. dynamic sizing append, remove
4. store heterogenous data type [1,'a',2.3] 
"""
"""
# Tuples
1. small brackets 
2. immutable, coordinates, rbg value.
3. data remains consistent throughout the program because they are immutable
"""