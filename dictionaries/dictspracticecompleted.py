#Complete the assignments below on dictionaries.

#Create a variable called 'nums' that holds a dict made up
#of the pairs "hello" and 2, "hi" and 1, and "howdy" and 4
nums = {"hello":2, "hi":1, "howdy":4}

#Create a dictionary with the variable 'names' that contains 4
#elements whose keys are your favorite teacher's names and
#the values are the classes you took with them
names = {
    "Semenuk":"Geometry",
    "Cullen":"Stats",
    "Kirchmeier":"Calculus",
    "Pointek":"Algebra"
}

#Print the two dicts we've created
print(nums)
print(names)

#Print the value paired with "hi" in 'nums', and choose a teacher
#to print their associated class in 'names'.
print(nums["hi"])
print(names["Cullen"])

#Print a check to see if "Guzauckas" is a key in 'names'
print("Guzauckas" in names)

#Change the value associated with 'hello' in 'nums' to 7
nums["hello"] = 7

#Add another teacher:class pair to 'names'
names.update({"Vigneault":"Algebra 2"})

#Remove the pair with the key 'hi' from 'nums'
nums.pop("hi")

#Clear the dict 'nums'
nums.clear()

#Print out all of the dicts you've defined so far
print(nums)
print(names)

#Use f-strings like I did on line 70 of dicts.py to print the lengths
#of each of our dicts
print(f"There are {len(nums)} elements in nums")
print(f"There are {len(names)} elements in names")