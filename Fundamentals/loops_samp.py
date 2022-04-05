def show_nested_loop():
    # nested loop
    #for loop for variable in variable
    numbers = [5,2,5,2,2]
    for x_count in numbers:
        output = ''
        for count in range(x_count):
            output +='x'
        print (output)

def show_while_loop():
    #while loop
    i=1
    while i<=5:
        print('*' * i)
        i=i+1
    print("done")


def using_else_in_while():
    #using else in while loop
    secrect_number = 9
    guess_limit = 3
    guess_count=0
    while  guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count +=1
        if guess == secrect_number:
            print("You won")
            break # to terminate the loop
    else:
        print('Sorry you failed')
