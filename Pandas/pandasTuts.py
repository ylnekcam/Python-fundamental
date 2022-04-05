import pandas as pd

def df_init_create_from_list():
    # initialize list of lists
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['Name', 'Age'])
    # print dataframe.
    print(df)


# Python code demonstrate creating
# DataFrame from dict narray / lists
# By default addresses.
def df_init_create_from_dict():
    # initialize data of lists.
    data = {'Name':['Tom', 'nick', 'krish', 'jack'],
            'Age':[20, 21, 19, 18]}
    # Create DataFrame
    df = pd.DataFrame(data)
    # Print the output.
    print(df)


def df_init_create_from_list_in_dict_by_index():
    # Python code demonstrate creating
    # pandas DataFrame with indexed by
    # initialize data of lists.
    data = {'Name':['Tom', 'Jack', 'nick', 'juli'],
            'marks':[99, 98, 95, 90]}
    
    # Creates pandas DataFrame.
    df = pd.DataFrame(data, index =['rank1',
                                    'rank2',
                                    'rank3',
                                    'rank4'])
    
    # print the data
    print(df)


def df_init_create_from_list_of_dict():
    # Initialize data to lists.
    data = [{'a': 1, 'b': 2, 'c':3},
            {'a':10, 'b': 20, 'c': 30}]
    
    # Creates DataFrame.
    df = pd.DataFrame(data)
    # Print the data
    print(df)


def df_init_create_from_list_of_dict_row_idex():
    # Initialize data of lists
    data = [{'b': 2, 'c':3}, {'a': 10, 'b': 20, 'c': 30}]
    # Creates pandas DataFrame by passing
    # Lists of dictionaries and row index.
    df = pd.DataFrame(data, index =['first', 'second'])
    # Print the data
    print(df)


def df_init_create_from_list_of_dict_col_and_row_idex():
    # Initialize lists data.
    data = [{'a': 1, 'b': 2},
            {'a': 5, 'b': 10, 'c': 20}]
    
    # With two column indices, values same
    # as dictionary keys
    df1 = pd.DataFrame(data, index =['first',
                                    'second'],
                        columns =['a', 'b'])
    
    # With two column indices with
    # one index with other name
    df2 = pd.DataFrame(data, index =['first',
                                    'second'],
                        columns =['a', 'b1'])
    
    # print for first data frame
    print (df1, "\n")
    
    # Print for second DataFrame.
    print (df2)


def df_init_create_from_list_using_zip():
    # List1
    Name = ['tom', 'krish', 'nick', 'juli']
    
    # List2
    Age = [25, 30, 26, 22]
    
    # get the list of tuples from two lists.
    # and merge them by using zip().
    list_of_tuples = list(zip(Name, Age))
    
    # Assign data to tuples.
    print(f'list of tuples list(zip(Name, Age)): {list_of_tuples}')
    
    # Converting lists of tuples into
    # pandas Dataframe.
    df = pd.DataFrame(list_of_tuples,
                    columns = ['Name', 'Age'])
        
    # Print data.
    print(f'data frame:{df}')


def df_init_create_from_dict_series():
    # Initialize data to Dicts of series.
    d = {'one' : pd.Series([10, 20, 30, 40],
                        index =['a', 'b', 'c', 'd']),
        'two' : pd.Series([10, 20, 30, 40],
                            index =['a', 'b', 'c', 'd'])}
    
    # creates Dataframe.
    df = pd.DataFrame(d)
    
    # print the data.
    print(f'dict_series data frame:{df}')