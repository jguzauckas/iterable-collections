#Complete the assignments below on tuples.

#Create a variable called 'nums' that holds a tuple
#made up of the numbers 23, 42.1, 55, and 0.1
nums = (23, 42.1, 55, 0.1)

#Here is a pre-made list of names:
l = ["John", "Jacob", "Jingleheimer", "Schmidt"]
#Use the tuple constructor to turn this list into a tuple with
#the variable name 'names'
names = tuple(l)

#Here is a string:
s = "I Love CS"
#Use the tuple constructor to turn this string into a tuple
#with the variable name 'cs'
cs = tuple(s)

#Print out all of the tuples you've defined so far
print(nums)
print(names)
print(cs)

#Print the second element of 'nums', the third element of 'names'
#and the 7th element of 'cs'. Remember zero indexing!
print(nums[1])
print(names[2])
print(cs[6])

#Use f-strings like I did on line 39 of tuples.py to print the lengths
#of each of our three tuples
print(f"nums has {len(nums)} elements")
print(f"names has {len(names)} elements")
print(f"cs has {len(cs)} elements")