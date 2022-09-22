#Complete the assignments below on sets.

#Create a variable called 'nums' that holds a set
#made up of the numbers 24, 7.66, 22, -5
nums = {24, 7.66, 22, -5}

#Here is a pre-made tuple of names:
t = ("Abby", "Madeline", "Evan", "Carnel")
#Use the set constructor to turn this tuple into a set with
#the variable name 'names'
names = set(t)

#Here is a string:
s = "I am in class"
#Use the set constructor to turn this string into a list
#with the variable name 'inclass'
inclass = set(s)

#Print the sets we've made so far
print(nums)
print(names)
print(inclass)

#Remove the value 22 from 'nums', and remove the last value of
#'names'
nums.discard(22)
names.pop()

#Add the value "Cullen" to 'names'
names.add("Cullen")

#Here is a pre-created tuple of names:
t = ("Semenuk", "Leroux")
#Add these names to the end of 'names'
names.update(t)

#Print out all of the sets you've defined so far
print(nums)
print(names)
print(inclass)

#Use f-strings like I did on line 73 of sets.py to print the lengths
#of each of our three sets
print(f"There are {len(nums)} elements in nums")
print(f"There are {len(names)} elements in names")
print(f"There are {len(inclass)} elements in inclass")