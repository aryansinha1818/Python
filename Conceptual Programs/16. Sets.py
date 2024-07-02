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