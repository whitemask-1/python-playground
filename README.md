# Python Playground

This repository serves as a personal learning journal documenting my journey of learning Python.

Rather than following isolated tutorials, this repo captures my understanding as it develops through:
- Small experiments and exploratory scripts
- Concept-focused exercises
- Mini-projects built to internalize core ideas
- Iterative refinements and refactors as knowledge improves

The goal is not perfection, but progression—using code as a medium to think, test, fail, and improve.

---

## Learning Index

## Day 1: Python Fundamentals

### Core Concepts
- **Hello World** (`hello-world.py`): First Python program, print statements, basic syntax
- **Data Types** (`data-types.py`): 
  - Primitive types: `int`, `float`, `str`, `bool`
  - Type checking with `type()`
  - Type conversion and casting
  - Understanding mutable vs immutable types

- **Numbers & Mathematical Operations** (`numbers+mathematical-ops.py`):
  - Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
  - Order of operations (PEMDAS)
  - Integer vs float division
  - Modulo operations and exponentiation

- **Strings** (`strings.py`):
  - String creation and indexing
  - String slicing and concatenation
  - String methods: `.upper()`, `.lower()`, `.strip()`, `.split()`, `.join()`
  - String formatting: f-strings, `.format()`
  - Escape characters and raw strings

- **Booleans & Conditionals** (`bools+conditionals.py`):
  - Boolean values: `True`, `False`
  - Comparison operators: `==`, `!=`, `<`, `>`, `<=`, `>=`
  - Logical operators: `and`, `or`, `not`
  - `if`, `elif`, `else` statements
  - Nested conditionals and truthiness

### Projects
- **Report Card (FreeCodeCamp)** (`report-card(FCC).py`): 
  - Applied conditionals for grade calculation
  - User input handling
  - Conditional logic and decision trees

### Key Concepts Learned
- Python syntax and indentation
- Variable naming conventions
- Type system and dynamic typing
- Control flow with conditionals
- String manipulation and formatting
- Basic I/O with `print()` and `input()`

---

## Day 2: Functions, Scope & Built-in Tools

### Functions & Scope
- **Functions** (`func.py`):
  - Function definition with `def`
  - Parameters and arguments (positional, keyword, default)
  - Return values vs `None`
  - Docstrings and function documentation
  - `*args` and `**kwargs` for variable arguments

- **Scope** (`scope.py`):
  - Local vs global scope
  - `global` and `nonlocal` keywords
  - LEGB rule (Local, Enclosing, Global, Built-in)
  - Scope resolution and variable shadowing
  - Closure concepts

### Variables
- **Variables** (`variables.py`):
  - Variable assignment and reassignment
  - Multiple assignment
  - Variable naming best practices
  - Constants convention (UPPER_CASE)

- **Variable Exercises** (`var-exercises.py`):
  - Practical variable manipulation problems
  - Swapping variables
  - Accumulator patterns

### Built-in Functions
- **Built-in Functions** (`builtinfuncs.py`):
  - Common functions: `len()`, `sum()`, `min()`, `max()`, `abs()`
  - Type conversion: `int()`, `float()`, `str()`, `bool()`
  - Input/output: `input()`, `print()`
  - Utility functions: `range()`, `sorted()`, `reversed()`
  - `help()` and `dir()` for introspection

### Projects
- **Caesar Cipher** (`ceasar-cipher.py`):
  - String manipulation and character shifting
  - Modulo arithmetic for wrapping
  - Function composition
  - Encryption/decryption logic

### Key Concepts Learned
- Function design and modularity
- Scope and namespace management
- DRY principle (Don't Repeat Yourself)
- Code organization and reusability
- Working with Python's standard library

---

### Day 3: Advanced Data Structures, Functional Programming & 3D Visualization

### Loops + Sequences
- **Lists** (`lists.py`): Mutable sequences, list methods, slicing, and common operations
- **Tuples** (`tuples.py`): Immutable sequences, tuple packing/unpacking, use cases
- **Ranges** (`ranges.py`): Efficient sequence generation with `range()`
- **Loops** (`loops.py`): `for` and `while` loops, `break`, `continue`, loop patterns
- **Enumerate & Zip** (`enumerate+zip.py`): Iterate with indices, combine iterables
- **List Comprehensions** (`list-comprehensions.py`): Concise list creation, filtering, nested comprehensions
- **Lambda Functions** (`lambda-funcs.py`): Anonymous functions, `map()`, `filter()`, `reduce()`, functional programming

### Complex Numbers & Mathematical Concepts
- **Complex Numbers** (`complex-nums`): Complex number operations, magnitude, conjugates
- **RPG Character System** (`rpg-character.py`): Applied programming with classes and game logic

### Matplotlib Experiments

#### Calculus 3 Homework Visualizations
- **3D Plotting Series** (`3d-plot1.py` through `3d-plot5.py`): 
  - Surface plots and parametric surfaces
  - Vector fields in 3D space
  - Multiple plot configurations
  - Coordinate system transformations

#### Cool Scripts
- **Mandelbulb Fractal** (`mandelbulb.py`): 
  - 3D fractal generation using spherical coordinates
  - Cartesian ↔ Spherical coordinate transformations
  - Iterative escape-time algorithms
  - 3D animation with matplotlib
  - Depth sorting for solid appearance
  - Dynamic camera movements

- **Fractal Collection** (`fractal-collection.py`):
  - Multiple fractal types (Mandelbrot, Burning Ship, Tricorn)
  - Functional programming with lambda functions
  - Complex number mathematics and iterations
  - Using `map()` for parallel computation
  - Escape-time coloring algorithms
  - Animated fractal showcase

- **3D Plot Generator** (`3d-plot-generator.py`):
  - Interactive 3D surface generation
  - Customizable mathematical functions
  - Real-time visualization tools

### Key Concepts Learned
- Functional programming paradigms (`map`, `filter`, `reduce`, lambda functions)
- Complex number arithmetic and fractal mathematics
- 3D coordinate systems and transformations
- Animation techniques with matplotlib
- Iterative algorithms and escape-time methods
- Higher-order functions and function composition
- Depth sorting and 3D rendering techniques

---

## Day 4: Dictionaries, Sets, Modules & Data Management

### Dictionaries and Sets
- **Dictionaries** (`dictionaries.py`):
  - Key-value pair data structure
  - Dictionary creation: literals, `dict()`, `fromkeys()`
  - Accessing values: bracket notation, `.get()` method
  - Dictionary methods: `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`
  - Nested dictionaries for complex data
  - Dictionary use cases and when to use them

- **Dictionary Looping** (`dictionary-looping.py`):
  - Iterating over keys, values, and items
  - Dictionary comprehensions: `{k: v for k, v in ...}`
  - Filtering dictionaries with conditions
  - Transforming dictionary data
  - Combining multiple dictionaries

- **Sets** (`sets.py`):
  - Unordered collections of unique elements
  - Set creation and literals: `{1, 2, 3}`
  - Set operations: union, intersection, difference, symmetric difference
  - Set methods: `.add()`, `.remove()`, `.discard()`, `.pop()`
  - Mathematical set operations: `|`, `&`, `-`, `^`
  - Use cases: removing duplicates, membership testing, set algebra

### Input Handling & Data Processing
- **List Inputs & Unpacking** (`list-inputs-unpacking.py`):
  - Collecting multiple inputs into lists
  - Unpacking lists to multiple variables
  - Using `.split()` for parsing input strings
  - Handling whitespace with default `.split()`
  - Type conversion during unpacking
  - Extended unpacking with `*` operator

- **Number Pattern Generator** (`num-pattern.py`):
  - Pattern generation algorithms
  - Nested loops for 2D patterns
  - String formatting for visual output

- **PIN Extractor** (`pin-extractor.py`):
  - String manipulation and parsing
  - Extracting specific data patterns
  - Input validation and error handling

### Projects
- **Medical Validator** (`medical-validator.py`):
  - Dictionary-based data validation
  - Checking required fields and data types
  - Applied dictionaries for structured data
  - Real-world data validation patterns

### Libraries and Modules
- **Custom Library** (`library.py`):
  - Creating reusable functions
  - Module organization and imports
  - Code modularity and DRY principles
  - Building your own function library

### Personal Movie Tracker (PMT)
- **Project Planning** (`PMT_README.md`):
  - Comprehensive project roadmap
  - Designed multi-phase development plan
  - Core features: add movies, track watch status, ratings, statistics
  - Future enhancements: data persistence (JSON), search/filter, matplotlib visualizations
  - Planned integrations: OMDB API, genre analysis, recommendation system
  - Learning progression from CLI to potential GUI
  - Applied dictionary concepts to real-world tracking problem

### Key Concepts Learned
- **Data Structures**: Dictionaries vs sets vs lists - when to use each
- **Key-Value Storage**: Efficient data organization and retrieval
- **Set Theory**: Mathematical operations on collections
- **Dictionary Comprehensions**: Concise dictionary transformations
- **Input Processing**: Parsing and validating user input
- **Code Organization**: Creating reusable modules and libraries
- **Project Planning**: Breaking large projects into phases
- **Real-World Applications**: Building tools for personal use

---

## Day 5: Error Handling & Debugging

### Error Handling Fundamentals
- **Exception Handling** (`exception-handling.py`):
  - `try/except` blocks for catching errors
  - Multiple except clauses for different exception types
  - `else` clause for code that runs when no exception occurs
  - `finally` clause for cleanup code that always runs
  - Exception object access and error messages

- **Common Errors** (`errors.py`):
  - `ValueError` - Invalid values for correct type
  - `TypeError` - Wrong data type operations
  - `ZeroDivisionError` - Division by zero
  - `IndexError` - List index out of range
  - `KeyError` - Dictionary key doesn't exist
  - `FileNotFoundError` - File operations on non-existent files
  - `AttributeError` - Invalid attribute access

- **Raising Exceptions** (`raise.py`):
  - Using `raise` keyword to throw exceptions
  - Creating custom error messages
  - Re-raising exceptions after logging
  - When to raise vs. handle exceptions
  - Input validation with custom exceptions

- **Debugging Techniques** (`debugging.py`):
  - Using `print()` statements for debugging
  - Python debugger (`pdb`) basics
  - Tracing execution flow
  - Identifying and fixing logic errors
  - Stack traces and error messages

### Projects
- **User Configuration Validator** (`userconfig.py`):
  - Comprehensive input validation with error handling
  - Type checking and range validation
  - Required field verification
  - Graceful error recovery with user-friendly messages
  - Applied exception handling to real-world scenario
  - Defensive programming patterns

### Key Concepts Learned
- **Exception Hierarchy**: Understanding Python's exception class structure
- **Error vs Exception**: Syntax errors vs runtime exceptions
- **Defensive Programming**: Validating inputs before processing
- **Graceful Degradation**: Handling errors without crashing
- **Error Propagation**: When to catch vs. let errors bubble up
- **Debugging Workflow**: Systematic approach to finding and fixing bugs
- **User Experience**: Providing helpful error messages to users

---

## Day 6: Object-Oriented Programming & Classes

### Classes and Objects Fundamentals
- **Classes and Objects** (`classes+objects.py`):
  - Class definition with `class` keyword
  - `__init__()` constructor method for initialization
  - Instance attributes (self.attribute)
  - Creating objects/instances from classes
  - Understanding `self` parameter
  - Class vs instance concepts

- **Methods and Attributes** (`methods+attributes.py`):
  - Instance methods that operate on object data
  - Accessing attributes with `self.attribute`
  - Calling methods on objects: `object.method()`
  - Method parameters and return values
  - Encapsulation - keeping data and methods together

- **Special Methods** (`special-methods.py`):
  - `__str__()` for human-readable string representation
  - `__repr__()` for developer-friendly representation
  - `__len__()` for custom length behavior
  - `__add__()` for custom addition operator
  - Dunder methods (double underscore) overview
  - Operator overloading basics

- **Dynamic Attribute Handling** (`dynamic-attr-handling.py`):
  - `getattr(object, name)` - get attribute by string name
  - `setattr(object, name, value)` - set attribute dynamically
  - `hasattr(object, name)` - check if attribute exists
  - `delattr(object, name)` - delete attribute
  - Dynamic attribute access patterns

### Projects

- **Planet Class** (`planets.py`):
  - Created Planet objects with name, type, and star attributes
  - Implemented `orbit()` method to describe planetary motion
  - Custom `__str__()` for formatted planet descriptions
  - Input validation with `isinstance()` checks
  - Raised `TypeError` for wrong types, `ValueError` for empty strings
  - Caught exceptions during object creation to keep program running
  - Applied error handling patterns in OOP context

- **Musical Instruments** (`musical-instruments.py`):
  - Built MusicalInstrument class with play() method
  - Different instrument types produce different sounds
  - Practice with instance methods and attributes

- **Email Simulator** (`email-sim.py`):
  - Created Email class with sender, recipient, subject
  - Implemented send() and receive() methods
  - Simulated email operations with object-oriented design

- **ISBN Validator** (`ISBN-validator.py`):
  - Validated ISBN-10 and ISBN-13 formats
  - Parsed comma-separated input values
  - Checked for proper format (commas present)
  - Validated length parameter is a number
  - Converted string digits to integer list with list comprehension
  - Applied checksum algorithms for ISBN validation
  - Comprehensive error handling with user-friendly messages
  - Input validation: format checking, type validation, value ranges

### Key Concepts Learned
- **Object-Oriented Programming**: Organizing code with classes and objects
- **Encapsulation**: Bundling data and methods that work on that data
- **Instance vs Class**: Understanding object instances vs class definitions
- **Constructor Pattern**: Using `__init__()` to set up object state
- **Method Calls**: How objects interact through methods
- **Special Methods**: Customizing Python's built-in operations
- **Input Validation in OOP**: Enforcing rules in constructors
- **Error Handling in Classes**: Raising exceptions vs catching them
- **Separation of Concerns**: Class validates, caller handles errors
- **List Comprehensions with Conversion**: Processing digit strings efficiently

---