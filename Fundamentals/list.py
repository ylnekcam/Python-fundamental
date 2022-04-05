#list
names=['John','Bob','Mac','Nancy','Emer']
print(names[0])
print(names[-2])
#range
print(names[2:4])#index 4 is no return
#modify the list
names[0]='jon'
print (names[0])


#find the greater number

numbers = [3,6,2,3,4,8,1]
max = numbers[0]
#for loop x can change to any variable
for x in numbers:
    if x > max:
        max=x
print (max)

#2D list
#define the list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#accessing the list matrix [list count][index]
print(matrix[0][1])
#modify the data on the list
matrix[0][1]=20
print (matrix[0][1])

#iterate all the item on list using nested loop
for row in matrix:
    for item in row:
        print (item)

#list method

#append-add item on the list on the last item
numbers.append(20)
print(numbers)

#insert(index,value) - add item on any index you want
numbers.insert(0,10)
print(numbers)

#remove(value) 
numbers.remove(2)
print(numbers)
#remove last value using pop()
numbers.pop()
print(numbers)

#get the index of list value index(value) if no value you will get an error
print(numbers.index(6))

#check if value was on the list
findNumber=4
print(findNumber in numbers)

#count the item with same value
print(numbers.count(3))

#sorting
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)

#copy
number2=numbers.copy()
numbers.append(10)
print (f"copy of numbers before append {number2}")
print(f"numbers after append{numbers}")

#clear
numbers.clear()
print(numbers)