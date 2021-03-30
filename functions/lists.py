number_list = [1,3,5,7]
names_list = ["Kate", "Jim", "Jim", "Palina", "Kevin"]
print(number_list)
print(names_list[2])

# method that puts two separate lists together
# names_list.extend(number_list)
print(names_list)

# method that adds element to the end of the list
names_list.append("Lola")
print(names_list)

# method that inserts the specific element to specific location in the list

names_list.insert(1, "Stephan")
print(names_list)

# removing specific element
names_list.remove("Lola")
print(names_list)

# to get rid of all elements
# names_list.clear()

# method pop removes the last element from the list
names_list.pop()
print(names_list)

# method that counts the number of same element in the list
print(names_list.count("Jim"))

# method to find the index of the element

print(names_list.index("Palina"))

# method to sort the list in the alphabetical order
# NOTE! you can not put sort in PRINT
names_list.sort()
print(names_list)

# to reverse a string
names_list.reverse()
print(names_list)




