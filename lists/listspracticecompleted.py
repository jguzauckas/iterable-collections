#Complete the assignments below on lists.

#Create a variable called 'nums' that holds a list
#made up of the numbers 17, 22.1, 44, 333
nums = [17, 22.1, 44, 333]

#Here is a pre-made tuple of names:
t = ("Guzauckas", "Cawley", "Lorenzet", "Kirchmeier")
#Use the list constructor to turn this tuple into a list with
#the variable name 'names'
names = list(t)

#Here is a string:
s = "I Love CS"
#Use the list constructor to turn this string into a list
#with the variable name 'cs'
cs = list(s)

#Print the first element of 'nums', the fourth element of 'names'
#and the 6th element of 'cs'. Remember zero indexing!
print(nums[0])
print(names[3])
print(cs[6])

#Change the second value of 'nums' to 10, change the third value of
#'names' to "Newton", and change the fourth value of 'cs' to 'i'
nums[1] = 10
names[2] = "Newton"
cs[3] = 'i'

#Remove the value 44 from 'nums', and remove the first value of
#'names'
nums.remove(44)
names.pop(0)

#Add the value "Cullen" in the second slot of 'names', and add
#the value '!' to the end of 'cs'
names.insert(1, "Cullen")
names.append('!')

#Here is a pre-created tuple of names:
t = ("Semenuk", "Leroux")
#Add these names to the end of 'names'
names.extend(t)

#Print out all of the lists you've defined so far
print(nums)
print(names)
print(cs)

#Use f-strings like I did on line 64 of lists.py to print the lengths
#of each of our three lists
print(f"There are {len(nums)} elements in nums")
print(f"There are {len(names)} elements in names")
print(f"There are {len(cs)} elements in cs")