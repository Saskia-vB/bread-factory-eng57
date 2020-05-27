from general_function import return_formatted_name


# test set up
known_input = '    filipe    '
expected_output = 'Filipe'
#
# # test execution
print("Testing function return_formatted_name() with '     filipe     ' --> 'Filipe'")
print(return_formatted_name(known_input) == (expected_output))

# testing say_hello()

from general_function import say_hello_name

known_input_say_hello = 'Hussain  '
expected_output_say_hello = 'hello Hussain'

print("Testing function say_hello_name() with 'hello Hussain  ' --> 'hello Hussain'")
print(say_hello_name(known_input_say_hello) == (expected_output_say_hello))

print(say_hello_name(known_input_say_hello))