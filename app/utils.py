
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44

    """
    return '${:,.2f}'.format(my_price)

#imports a function cleanly with the use of a main conditional

#    Docstring = tells us what this function is about.
#    What its responsibilities are
#    What the parameters are about
#    What datatypes the parameters are
#    What this function will return
#    Example of invoking the function
#
#    Invoke like this: to_usd(9.9999)

#testing to see if the function works properly (demonstrating the concept of the function)
#if this code is in the global scope of a file we're trying to import from
#...it will throw erros when we try to run those other files
#(having unintended side effects (going through all this code before going through the called file))

#price = input ("Please choose a price like 4.9999: ")
#print(to_usd(float(price)))


#Solution:  NEST UNDER A MAIN CONDITIONAl
#minimize the amount of additional code in a global function
#structure testing code under the main conditional

if __name__ == "__main__":
    # keeps our global scope clean when running this file  
    # nesting code in the main condition will
    # allow other scripts to cleanly import functions from this file
    # without running this code

    # this code still gets to run when we invoke the script from the command line
    price = input("Please choose a price like 4.9999: ")

    print(to_usd(float(price)))