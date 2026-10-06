students = ["kaisamba", "john", "jabbie"]
print (students)

# Accessing elements in the list by their index
print (f"my best friend is {students[0]}")
print (f"my best friend is {students[1]}")
print (f"my best friend is {students[2]}")

# Get the index of an element in the list
print (students.index("kaisamba"))
print (students.index("john"))
print (students.index("jabbie"))

# know the number of items in a list
print (f"The total items in the list is {len(students)}")

# Add items to the list
students.append("Foday")
print (students)
students += ["Musa", "Sulaiman", "Gassam"]
print (students)
students.insert(4, "Abdulai")
print (students)

# Extending a list
fruits = ["banana", "mango", "orange"]
students.extend(fruits)
print (students)

# Removing an item from a list
fruits.remove("banana")
print (fruits)

fruits.remove("mango")
print (fruits)
fruits.remove("orange")

students.pop()
students.pop()
thirditem = students.pop()
print(thirditem)
