#defining a function
#def nameof_function():
#at the end of function your must have 2 space

#function with parameter, but function can also have no parameters or multiple parameters
def greet_user(name,age):
    print(f'Hi there {name}!')
    print(f'You are {age} years old')


print('Start')
greet_user("John",20) #call the function, make sure you define your function first before calling it
greet_user("Mary",25) #positional argument must have an argument because you define the function with parameters
greet_user(age=25,name="Nancy")#keyword argument if you don't know the order of parameters of the function
greet_user("Nancy",age=13)# if you use both keyword and positional argument use positional first
print('Finish')


#function with return by default it return none
def square(number):
    return number * number


print(square(3))