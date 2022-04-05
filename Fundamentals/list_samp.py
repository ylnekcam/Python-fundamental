
def list_init_get_single_data():
    #list
    names=['John','Bob','Mac','Nancy','Emer']
    print(names[0])
    print(names[-2])
    #range
    print(names[2:4])#index 4 is no return
    #modify the list
    names[0]='jon'
    print (names[0])


def list_init_find_max():
    #find the greater number
    numbers = [3,6,2,3,4,8,1]
    max = numbers[0]
    #for loop x can change to any variable
    for x in numbers:
        if x > max:
            max=x
    print (max)


def list_init_2d_list():
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


def list_with_nested_loop():
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


def list_method():
    #list method
    print('numbers = [3,6,2,3,4,8,1,3,4,5,6,7,8,9,4,5,4,6,7,8,9,9]')
    numbers = [3,6,2,3,4,8,1,3,4,5,6,7,8,9,4,5,4,6,7,8,9,9]
    max = numbers[0]
    #for loop x can change to any variable
    for x in numbers:
        if x > max:
            max=x
    print (max)
    #append-add item on the list on the last item
    print(f'append(20):{numbers.append(20)}')

    #insert(index,value) - add item on any index you want
    print(f'insert(0,10):{numbers.insert(0,10)}')

    #remove(value) 
    print(f'remove(2):{numbers.remove(2)}')

    #remove last value using pop()
    print(f'remove last value using pop():{numbers.pop()}')

    #get the index of list value index(value) if no value you will get an error
    print(f'get the index(6):{numbers.index(6)}')
    
    #check if value was on the list
    findNumber=4
    print(f'findnumber=4 in the list: {findNumber in numbers}')

    #count the item with same value
    print(f'count item with same value using count(3):{numbers.count(3)}')

    #sorting
    print(f'sort():{numbers.sort()}')
    print(f'reverse():{numbers.reverse()}')

    #copy
    number2=numbers.copy()
    numbers.append(10)
    print (f"copy of numbers before append number2:{number2}")
    print(f"numbers after append(10){numbers}")

    #clear
    print(f'clear():{numbers.clear()}')


