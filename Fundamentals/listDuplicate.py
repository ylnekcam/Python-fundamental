#remove duplicate
numbers = [2,2,3,1,6,8,9,5,7,8,9,0,7,5,4,3,4,4,9,9,9]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print (uniques)