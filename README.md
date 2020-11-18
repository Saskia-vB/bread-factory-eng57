# Factory of Alentejo Bread :taco:

### Description of project

This small project looks at using functions and TDD.
We're also implementing Agile and Scrum principles.

Topics covered include:
- functions
- TDD
- Documentation
- Agile
- Scrum

### Functions
Functions are like people at work. They have one job!
This makes it easier to test.

#### How do they work?
1) We need to define them,
2) then call them.
3) They run the block of code that is idented.

Other functionality:
- they can take in arguments to be dynamic and morph the output.

If a variable is like a bow, you name it and place things inside. The bow does not interact with your stuff. i.e., if you name your box 'books' and place some potatoes inside, you do not get french fries.

A **function** is like a machine. It can interact with things you put inside. It can take inputs and follow a set of instructions (AKA the block of code)

#### Why functions?
Because it keeps our code DRY:
- don't
- repeat
- yourself

Allows us to call said function to do the actions in the block.

#### best practices of function
- name convention in python is like a variable, lower_case_underscore()
- IT DOES ONE JOB!
- DON'T PRINT IN FUNCTIONS -> makes it hard for the program to use or test
- separation of concerns: where you design is not where you produce
    - helps remove signle point of failure in code,
    - makes code more maintainable

## Basis of a test
A test has know or controlled inputs and expect outputs.
All it is, is an assertion.

Unit test is the testing of one single function.

You give it a known input, and you assert for expected output.

Run it, get True or False.


## TDD & testing

Testing individual blocks of code to verify functionality

pros:
- avoids technical debt
- know your code is working
- Understanding of your code improves
- more re-usable/scalable code
- easier to debug
- easier to maintain
- reduce costs
- reduce spaghetti code (unreadable or hard to understand code)
- attract better talent for projects

cons:
- you have to write the tests
- bad tests will result in bad code

Unit Testing
- tests a single part of code or function
- relates to user stories

Integration testing
- tests the entire program or system as a whole

Functions
- functions are like people at work: one job
- easier to test functions doing only one job

how do functions work?
- Define a method ML:
    def example_function(param):
    return something
- define and call a method to run blocks of code
- whereas variables are containers, functions are "cookers"
- they can take in arguments or parameters (but are not required to)
- they are dynamic and can morph the output
ML:
     mr_miyagi_question = input()
     functional_miyagi(mr_miyagi_question)
A function is like a machine

It can interact with things, take input and follow a set of instructions

#### Why functions - reusable code (DRY)

###### Best practices for functions
- Naming conventions, lower case, python_case
- Call with () e.g my_function()
- Separation of concerns
- exists at network, infrastructure and code level
- design separate from procedure, procedure separate from distribution, distribution separate from consumer
- opens and prevents a single point of failure
- makes code more maintainable
- DO NOT PRINT IN FUNCTIONS (ONLY TO DEBUG)

Basis of a test: has known or controlled inputs and expected outputs
Assertions: to assert if input results in expected output (True/False)
ML:
    known_input_1 = <name>
    expected_output = <result>
When importing from other files, best to import specific function
