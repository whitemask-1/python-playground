#Debugging is an essential skill, understanding foundational techniques can help identify and fix issues in code efficiently
#Debugging is the process of identifying, analyzing, and fixing bugs or errors in your code
#It involves examining the code, understanding flow, and using tools to pinpoint the source of issues

#Common Debugging Techniques:
#1. Print Statements: Inserting print statements at various points in the code to display variable
#   values and program flow to identify where things go wrong

def buggy_function(x):
    result = x * 2
    print(f"Debug: After multiplication, result = {result}")  # Print statement for debugging
    result += 10
    print(f"Debug: After addition, result = {result}")  # Print statement for debugging
    return result

#Interactive debugging with pdb:
import pdb

def another_buggy_function(y):
    pdb.set_trace()  # Set a breakpoint here
    total = 0
    for i in range(y):
        total += i
    return total
#By setting a trace with pdb, you can step through the code line by line, inspect variables, and evaluate expressions interactively
#Try running the functions above to see debugging in action
buggy_function(5)
another_buggy_function(5)
#You can open keywords for pdb using help keyword in the pdb interactive shell
#From there you can step through code, continue execution, and inspect variables

#IDE Debugging Tools:
#Most modern IDEs come with built-in debugging tools that allow you to set breakpoints, step through code, and inspect variables visually
#Familiarize yourself with the debugging features of your chosen IDE to enhance your debugging efficiency

#For VS Code, you can set breakpoints by clicking next to the line numbers and run the debugger from the Run and Debug panel
#To start debugging, press F5 or go to the Run menu and select Start Debugging
#To inspect variables, hover over them during a breakpoint or use the Variables panel in the debugger view
#To evaluate expressions, use the Debug Console to type in Python expressions and see their results during a debugging session
#To step through code, use the Step Over (F10), Step Into (F11), and Step Out (Shift+F11) commands in the debugger toolbar