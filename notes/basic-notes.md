## Basic Operations  
The print function can take multiple variables when they're divided by commas like:  

    print(x, y, z)

In python, range function is upper bounded:

    list(range(1, 10))

results in:

    [1, 2, 3, 4, 5, 6, 7, 8, 9]

An important function in python is **dir( )**. It returns all possible attributes of a type. In order to check the what the attribute does when called you can use the **help( )** function. Example:

    >>> dir(int)
    >>> help(int.to_bytes)
