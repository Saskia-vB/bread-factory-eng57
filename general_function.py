# recap function

# define a function

def say_hello_name(name):
    return(f'hello {name}')

# BAD!
def return_formatted_name(name):
    print(name.title().strip())
    return None

# Good:

def return_formatted_name(name):
    return name.title().strip()

 # print the return of the function not the function
f_name = return_formatted_name("   HUSSAIN   ")

print(say_hello_name(f_name))

# Basis of a test
def return_formatted_name(name):
    return name.title().strip()

# test set up
known_input = '    filipe    '
expected_output = 'Filipe'

# test execution
print("Testing function return formated name() with '     filipe     ' --> 'Filipe'")
print(return_formatted_name(known_input) == expected_out)

# testing say_hello()




