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