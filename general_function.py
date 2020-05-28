# recap function

# define a function

def say_hello_name(name):
    return(f'hello {name.title().strip()}')

# BAD!
# def return_formatted_name(name):
#     print(name.title().strip())
#     return None

# Good:

def return_formatted_name(name):
    return name.title().strip()

# print the return of the function not the function
# f_name = return_formatted_name("   HUSSAIN   ")


# print(say_hello_name(f_name))






