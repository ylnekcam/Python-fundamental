try:
    age=int(input("Age: "))
    income=2000
    risk = income/age
    print(age)
except ZeroDivisionError:
    print('Age can not be zero')
except ValueError:#this for input error value
    print('Invalid value')

