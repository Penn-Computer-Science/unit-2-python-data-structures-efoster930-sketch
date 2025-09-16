#Part 1: Lists
numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers[0],numbers[4],numbers[9])
numbers.append(11)
print(numbers)
numbers.pop(2)
numbers.insert(2,99)
print(numbers)

for item in numbers:
    int_item = int(item)
    if int_item%2 == 0:
        print(item)


#Part 2: Dictionaries
countries = {"Colombia":"Bogota","Canada":"Toronto","Chile":"Santiago","South Africa":"Capetown","Italy":"Rome"}
print(countries["Colombia"],countries["Canada"])
countries["Germany"] = "Berlin"
countries["Argentina"] = "Buenos Aires"
print(countries)
countries["Italy"] = "Florence"
print(countries["Italy"])
for item, value in countries.items():
    print(f"Country: {item}, Capital: {value}")

#Part 3: Sets
fruit_set = {"Banana","Apple","Mango","Oranges","Watermelon"}
print(fruit_set)
fruit_set.add("Green Apple")
print(fruit_set)
fruit_set.remove("Mango")
print(fruit_set)
friend_fruits = {"Pineapple","Apple","Grapes","Banana"}
intersection_set = fruit_set.intersection(friend_fruits)
print(intersection_set)
difference_set = fruit_set.difference(friend_fruits)
print(difference_set)

#Part 4: Colors
tuples_colors = ("Red","Blue","Green","Yellow","Purple")
print(tuples_colors[0],tuples_colors[4])
for color in tuples_colors:
    print(color)
tuple[0] = "Black"
#Raises a TypeError