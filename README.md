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

## Day 7: Advanced OOP & Daily Bugle Project

### Advanced OOP Concepts

- **Abstraction** (`abstraction.py`):
  - Abstract Base Classes (ABC) using `abc` module
  - `@abstractmethod` decorator for defining abstract methods
  - Abstract classes cannot be instantiated directly
  - Subclasses must implement all abstract methods
  - Creating simplified interfaces that hide complexity
  - Animal hierarchy: Dog, Cat, Fish with `make_sound()` method
  - PaymentProcessor system: PayPal and Stripe implementations
  - Understanding "what something does" vs "how it does it"

- **Polymorphism** (`polymorphism.py`):
  - Objects of different types responding to same method call
  - Method overriding in subclasses
  - Shape calculator with Circle, Rectangle, Square classes
  - Unified `area()` method across different shapes
  - Using `isinstance()` for type checking
  - Common interface pattern for different implementations

- **Inheritance** (`inheritance.py`):
  - Parent-child class relationships for code reuse
  - Using `super()` to call parent class methods
  - Person → Student → GraduateStudent hierarchy
  - Extending attributes through inheritance chain
  - Multiple inheritance with Teacher class (Person + Employee)
  - Method resolution order (MRO)
  - When to use inheritance vs composition

- **Encapsulation** (`oop+encapsulation.py`):
  - Controlling access to object data
  - Public attributes (normal access)
  - Protected attributes (`_attribute`) - convention for internal use
  - Private attributes (`__attribute`) - name mangling
  - Understanding `_ClassName__attribute` transformation
  - Preventing direct access to sensitive data

- **Getters and Setters** (`getters+setters.py`):
  - `@property` decorator for getter methods
  - `@attribute.setter` decorator for setter methods
  - Validation in setters before updating attributes
  - Read-only properties (getter without setter)
  - Computed properties that calculate values
  - Pythonic alternative to traditional getter/setter methods

- **Name Mangling** (`name-mangling.py`):
  - How Python mangles private attributes
  - `__private` becomes `_ClassName__private`
  - Accessing mangled attributes (not recommended)
  - Use cases for true privacy vs convention

### Practice Projects

- **Salary Tracker** (`salary-tracker.py`):
  - Encapsulation with private `__salary` attribute
  - `@property` getter for read-only salary access
  - Setter with validation for salary increases only
  - Demonstrates data protection and controlled modification
  - Name mangling in action

- **Character Stat Tracker** (`character-stat-track.py`):
  - Protected `_health` and `_mana` attributes
  - Property decorators for stat validation
  - Range checking (0-100 for stats)
  - Prevents invalid stat values
  - Game-style attribute management

### Daily Bugle News Scraper Project

**Goal**: CLI application that fetches NY Times top stories, displays details, and archives articles

#### Architecture (OOP Design)
- **Article Class**:
  - Stores article data: title, abstract, byline, url, published_date, section
  - `full_details` attribute for detailed API data
  - `__str__()` for basic display format
  - `display_full_details()` for comprehensive article view
  - `to_dict()` for JSON serialization
  - Timestamp tracking with `fetched_at`

- **NYTimesAPI Class**:
  - Handles all API interactions
  - API key from environment variable (`os.getenv()`)
  - `fetch_top_stories()` - Top Stories API endpoint
  - `fetch_article_details()` - Article Search API with URL filter
  - Error handling with `raise ConnectionError` for failed requests
  - Parses JSON responses into Article objects

- **NewsArchive Class**:
  - Manages collection of archived Article objects
  - `add_to_archive()` with type checking
  - `__len__()` returns article count
  - `__str__()` for archive summary
  - `display_all()` shows all archived articles with timestamps

- **DailyBugleMenu Class**:
  - Main application with menu-driven interface
  - Composition pattern: contains NYTimesAPI and NewsArchive instances
  - Dictionary dispatch for menu routing
  - Menu options: view stories, manage schedule, toggle scheduler, archives, exit

#### Features Implemented
- ✅ Fetch top 20 stories from NY Times Top Stories API
- ✅ Display headlines with numbered list
- ✅ User selects article to view full details
- ✅ Fetch comprehensive data from Article Search API
- ✅ Display lead_paragraph and snippet in formatted output
- ✅ Contextual archiving: save article after viewing details
- ✅ View all archived articles with fetch timestamps
- ✅ Dictionary dispatch pattern for clean menu handling
- ✅ Error handling: raise within methods, catch at appropriate levels
- ✅ Environment variable configuration for API key

#### API Integration
- **Top Stories Endpoint**: `https://api.nytimes.com/svc/topstories/v2/home.json`
  - Returns latest articles from home section
  - Provides basic info: title, abstract, byline, url, date
  
- **Article Search Endpoint**: `https://api.nytimes.com/svc/search/v2/articlesearch.json`
  - Uses filter query (`fq`) parameter to search by URL
  - Returns detailed content: lead_paragraph, snippet, multimedia

#### Usage Flow
1. View today's top stories (fetches from API)
2. Select article number to see full details
3. Fetch detailed information from Article Search API
4. Display comprehensive article with lead paragraph and snippet
5. Option to archive the article after viewing
6. Access old archives to review previously saved articles

#### Next Steps (Planned)
- [ ] Scheduler implementation with `schedule` library for 8am automated fetches
- [ ] JSON persistence: save/load archives to file
- [ ] Rich library integration for colored terminal output
- [ ] Section selection (world, business, technology, sports)
- [ ] Search within archived articles
- [ ] Export to Markdown or PDF

### Key Concepts Learned
- **Abstraction**: Hiding implementation details, exposing simplified interfaces
- **Polymorphism**: Same method call, different behaviors based on object type
- **Inheritance**: Code reuse through parent-child relationships
- **Encapsulation**: Protecting data with access control mechanisms
- **Property Decorators**: Pythonic getters/setters with validation
- **Composition over Inheritance**: Building complex systems by combining objects
- **Dictionary Dispatch**: Clean menu routing without if-elif chains
- **API Integration**: Working with REST APIs and environment variables
- **Error Handling Strategy**: Raising errors in handlers, catching at appropriate levels
- **OOP Design Patterns**: Single Responsibility, composition, encapsulation in practice

---

## Day 8: Enhancements to The Daily Bugle News System

#### What Changed
- **Added 6 APIs**
- **Rate limits now persist** across sessions (saves to `~/.dailybugle/rate_limit_state.json`)
- **User's API choice persists** (saves to `~/.dailybugle/config.json`)
- **Added Rich library** for colorful, formatted terminal UI
- **Rate limit dashboard** showing status of all 6 APIs

#### Implementation Highlights

**Persistent Rate Limiting**:
```python
class RateLimiter:
    def _save_state(self):
        """Save call counts to JSON after each API request"""
        with open(self.state_file, 'w') as f:
            json.dump(dict(self.api_calls), f, indent=2)
    
    def _load_state(self):
        """Load previous session's call counts on startup"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.api_calls = defaultdict(list, json.load(f))
```

**Rich Terminal UI**:
```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Colored tables
table = Table(show_header=True, box=box.ROUNDED)
table.add_column("#", style="cyan")
table.add_column("Title", style="bold yellow")

# Styled panels
panel = Panel(content, border_style="blue", box=box.ROUNDED)
console.print(panel)

# Interactive prompts
choice = Prompt.ask("[bold cyan]Your choice[/bold cyan]", choices=["1", "2", "3"])
```

**Config Persistence**:
```python
def _save_config(self):
    """Save user's preferred API to config file"""
    config = {
        'current_api': 'guardian',  # or whichever user selected
        'last_updated': datetime.now().isoformat()
    }
    with open(self.config_file, 'w') as f:
        json.dump(config, f, indent=2)
```

#### New Features
- **Option 5**: View rate limit status for all APIs in a table
- **Menu header**: Shows current API and remaining calls
- **Color-coded warnings**: Green/yellow/red based on quota usage
- **Loading spinners**: Visual feedback during API requests
- **Scheduled fetch**: Now uses your saved API preference

#### Key Learnings
- **State persistence**: Saving data between sessions using JSON
- **Rich library**: Professional CLI formatting with minimal code
- **User experience**: Visual feedback, colors, and helpful messages
- **Cross-script state**: Config shared between interactive and scheduled scripts

---

## Day 8: Common Data Structures & Algorithms + Daily Bugle Enhancements

### Common Data Structures

- **Static vs Dynamic Arrays** (`dynamic+static-arrays.py`):
  - **Static Arrays**: Fixed size, faster access (O(1)), stack-allocated memory
  - When to use: Known size in advance, frequent access, embedded systems
  - Limitations: Cannot grow or shrink, manual resizing requires copying
  - **Dynamic Arrays**: Flexible size, automatic resizing, heap-allocated
  - Python's list type is a dynamic array implementation
  - Time complexity: Access O(1), Insert at end O(1) average/O(n) worst, Insert middle O(n)
  - When to use: Unknown size, frequently changing data, continuous additions
  - Trade-offs: Resizing overhead vs memory flexibility

- **Linked Lists** (`linked-lists.py`):
  - **Singly Linked Lists**: Nodes with data and next pointer
  - Head node as entry point, tail points to None
  - Time complexity: Insert/delete at beginning O(1), at end O(n), search O(n)
  - When to use: Frequent insertions/deletions at beginning, unknown size
  - **Doubly Linked Lists**: Nodes with previous and next pointers
  - Bidirectional traversal, head and tail references
  - Time complexity: Insert/delete at both ends O(1), search O(n)
  - When to use: Need bidirectional traversal, operations at both ends
  - Trade-offs: More flexible but higher memory usage than singly linked

- **Maps, Hashmaps, and Sets** (`maps+hashmaps+sets.py`):
  - **Abstract Data Types (ADT)**: Conceptual representation without implementation details
  - **Maps**: Key-value pairs with unique keys
  - Operations: Insert, delete, lookup, update - all O(1) average
  - When to use: Associate unique keys with values, fast lookups
  - **Hashmaps**: Implementation using hash functions
  - Hash function generates index for array storage
  - Collision resolution: Chaining (linked lists), Open Addressing
  - Python's dict type is a hashmap implementation
  - **Sets**: Unordered collections of unique elements
  - Operations: Add, remove, membership testing - all O(1) average
  - When to use: Unique elements only, fast membership checks

- **Stacks and Queues** (`stacks+queues.py`):
  - **Stacks**: LIFO (Last In, First Out) data structure
  - Operations: Push O(1), Pop O(1), Peek O(1)
  - Elements added/removed from top only
  - When to use: Function call management, expression evaluation, backtracking
  - Python implementation: Using list with `append()` and `pop()`
  - **Queues**: FIFO (First In, First Out) data structure
  - Operations: Enqueue O(1), Dequeue O(1), Peek O(1)
  - Elements added at back, removed from front
  - When to use: Task scheduling, breadth-first search, request handling
  - Python implementation: Using `collections.deque` for efficiency

### Algorithms & Complexity Analysis

- **What Are Algorithms** (`what-are-algorithms.py`):
  - **Definition**: Unambiguous instructions for solving problems
  - Key characteristics: Definiteness (clear steps), Finiteness (terminates)
  - Language-independent design, implementation-specific execution
  - Correctness: Produces expected output for valid inputs
  - Efficiency: Time complexity (speed) and space complexity (memory)
  
- **Big O Notation**:
  - Describes worst-case performance as input size grows
  - Growth rate: How time/space requirements change with input
  - Focus on worst-case for understanding maximum inefficiency
  
- **Common Big O Classifications** (most to least efficient):
  - **O(1) - Constant Time**: Performance doesn't change with input size
    - Example: Accessing array element by index
  - **O(log n) - Logarithmic Time**: Divides problem in half each step
    - Example: Binary search in sorted array
  - **O(n) - Linear Time**: Performance scales linearly with input
    - Example: Iterating through array once
  - **O(n log n) - Linearithmic Time**: Efficient sorting algorithms
    - Example: Merge sort, Quick sort
  - **O(n²) - Quadratic Time**: Nested loops over input
    - Example: Bubble sort, nested iteration
  - **O(2ⁿ) - Exponential Time**: Doubles with each input increase
    - Example: Recursive Fibonacci without memoization
  - **O(n!) - Factorial Time**: Grows factorially with input
    - Example: Generating all permutations
  
- **Problem-Solving Strategies** (`problem-solving.py`):
  1. **Understand the Problem**: Read carefully, identify input/output, clarify ambiguities
  2. **Choose the Right Data Structure**: Analyze problem requirements, consider time complexity
  3. **Plan Your Approach**: Break into smaller parts, outline steps, consider edge cases
  4. **Implement the Solution**: Write clean code, use built-ins, comment logic, test samples
  5. **Analyze Complexity**: Evaluate Big O for time and space, optimize if needed
  - Problem-solving is iterative: revisit and refine based on testing
  - Regular practice improves pattern recognition and efficiency

### Daily Bugle News System Enhancements

#### What Changed
- **Added 6 APIs**: Expanded from single NY Times API to multi-provider system
- **Rate limits now persist** across sessions (saves to `~/.dailybugle/rate_limit_state.json`)
- **User's API choice persists** (saves to `~/.dailybugle/config.json`)
- **Added Rich library** for colorful, formatted terminal UI
- **Rate limit dashboard** showing status of all 6 APIs

#### Implementation Highlights

**Persistent Rate Limiting**:
```python
class RateLimiter:
    def _save_state(self):
        """Save call counts to JSON after each API request"""
        with open(self.state_file, 'w') as f:
            json.dump(dict(self.api_calls), f, indent=2)
    
    def _load_state(self):
        """Load previous session's call counts on startup"""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                self.api_calls = defaultdict(list, json.load(f))
```

**Rich Terminal UI**:
```python
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

# Colored tables
table = Table(show_header=True, box=box.ROUNDED)
table.add_column("#", style="cyan")
table.add_column("Title", style="bold yellow")

# Styled panels
panel = Panel(content, border_style="blue", box=box.ROUNDED)
console.print(panel)

# Interactive prompts
choice = Prompt.ask("[bold cyan]Your choice[/bold cyan]", choices=["1", "2", "3"])
```

**Config Persistence**:
```python
def _save_config(self):
    """Save user's preferred API to config file"""
    config = {
        'current_api': 'guardian',  # or whichever user selected
        'last_updated': datetime.now().isoformat()
    }
    with open(self.config_file, 'w') as f:
        json.dump(config, f, indent=2)
```

#### New Features
- **Option 5**: View rate limit status for all APIs in a table
- **Menu header**: Shows current API and remaining calls
- **Color-coded warnings**: Green/yellow/red based on quota usage
- **Loading spinners**: Visual feedback during API requests
- **Scheduled fetch**: Now uses your saved API preference

### Key Concepts Learned
- **Data Structures**: Static vs dynamic arrays, linked lists, hash tables, stacks, queues
- **Abstract Data Types**: Conceptual interfaces vs concrete implementations
- **Big O Notation**: Asymptotic analysis, worst-case performance, growth rates
- **Algorithm Efficiency**: Time vs space complexity trade-offs
- **Problem-Solving Framework**: Systematic approach from understanding to optimization
- **State Persistence**: Saving data between sessions using JSON
- **Rich Library**: Professional CLI formatting with minimal code
- **User Experience**: Visual feedback, colors, and helpful messages
- **Cross-Script State**: Config shared between interactive and scheduled scripts
- **Multi-API Architecture**: Managing multiple news providers with unified interface

---

## Day 9: Algorithm Practice & Performance Awareness 🎯

**Date:** January 31, 2026

Dove into problem-solving with a focus on algorithmic thinking and performance optimization. Started exploring LeetCode problems to apply data structure knowledge in practical scenarios.

### What I Learned

**Time Complexity Trade-offs:**
- Discovered that `in` operator on lists is O(n), making nested loops O(n²)
- Hash sets provide O(1) average lookup time - critical for optimization
- Understanding the hidden cost of operations is crucial for writing efficient code

**Algorithm Patterns:**
- **Hash Map Pattern**: Storing complements/seen values for O(1) lookups
- **Divide and Conquer**: Breaking problems into smaller subproblems recursively
- **Binary Search**: Continued reinforcement of logarithmic time algorithms

**Problem-Solving Approach:**
- Getting working solution first, then optimizing
- Analyzing time and space complexity after implementation
- Recognizing when a data structure choice impacts performance significantly

### Code Written

```python
# Contains Duplicate - First working solution
def hasDuplicate(self, nums: List[int]) -> bool:
    num_cache = []
    for num in nums:
        if num in num_cache:  # O(n) lookup on list
            return True
        num_cache.append(num)
    return False
# Time: O(n²), Space: O(n)
```

### Key Takeaways

- **First solve, then optimize** - getting a working solution builds confidence
- **Data structure choice matters** - list vs. set can be the difference between O(n²) and O(n)
- **Comment complexity analysis** - helps reinforce understanding and aids future review
- Problem-solving is a skill that improves with consistent practice
- Array and string manipulation problems reinforce data structure fundamentals

**Focus Areas:** Hash tables, binary search, divide & conquer, complexity analysis

---

## Day 10: Advanced Data Structures - Graphs, Trees & Heaps 🌲

**Date:** February 1, 2026

Explored advanced data structures that model complex relationships and hierarchical data. Focused on graph theory, tree structures, and priority queues—foundational concepts for optimization algorithms and real-world system design.

### Core Concepts

**Graphs** (`graphs.py`):
- **Nodes (Vertices)**: Objects or entities in the network (users, cities, stations)
- **Edges (Links)**: Connections or relationships between nodes
- **Adjacent Nodes**: Directly connected by an edge, also called neighbors
- **Undirected Graphs**: Bidirectional edges (mutual friendships)
- **Directed Graphs**: Unidirectional edges (Twitter follows)
- **Weighted Graphs**: Edges with costs/weights (distances, time)
- **Unweighted Graphs**: All edges considered equal
- **Cyclic Graphs**: Contain paths that form loops
- **Acyclic Graphs**: No cycles (e.g., family trees)
- **Vertex Labeled Graphs**: Each node has unique identifier
- **Edge Labeled Graphs**: Each edge has label describing relationship
- **Disconnected Graphs**: Separate components not connected by any path

**Graph Representations** (`matrices+adjacency-lists.py`):
- **Adjacency Matrix**: 2D array where rows/columns represent vertices
  - Values indicate edges: 1 (edge exists) or 0 (no edge)
  - Weighted graphs store edge weights instead of 1
  - Time complexity: O(1) to check if edge exists between two nodes
  - Space complexity: O(V²) - inefficient for sparse graphs
  - Best for: Dense graphs, frequent edge existence checks
  
- **Adjacency List**: Dictionary or array storing neighbors for each node
  - Dictionary: `{'A': ['B', 'C'], 'B': ['A', 'D']}`
  - Array: `[['B', 'C'], ['A', 'D'], ...]`
  - Time complexity: O(N) to check edge (N = number of neighbors)
  - Space complexity: O(V + E) - efficient for sparse graphs
  - Best for: Sparse graphs, iterating over all neighbors quickly
  
- **Trade-off**: Matrices for fast edge lookup, lists for space efficiency and neighbor iteration

**Graph Traversal Algorithms** (`depth+breadth-first-search.py`):
- **Breadth-First Search (BFS)**:
  - Visits all neighbors before moving to next level
  - Implemented with queue (FIFO) data structure
  - Algorithm: Start at node → mark visited → add to queue → dequeue → visit unvisited neighbors → repeat
  - Use case: Finding shortest path in unweighted graphs
  - Time complexity: O(V + E) where V = vertices, E = edges
  - Space complexity: O(V) for queue (can be large for wide graphs)
  - Analyzes all nodes at each level before going deeper
  
- **Depth-First Search (DFS)**:
  - Follows each branch as deep as possible before backtracking
  - Implemented with recursion or stack (LIFO) data structure
  - Algorithm: Start at node → mark visited → push to stack → pop → visit unvisited neighbors → repeat
  - Use case: Detecting cycles, finding connected components, single solution problems
  - Time complexity: O(V + E)
  - Space complexity: O(V) for visited set + O(H) for recursion stack (H = height)
  - More memory efficient than BFS for graphs with large branching factor
  - Does not guarantee shortest path in unweighted graphs
  - **Key insight**: `visited` set is shared across all recursive calls (passed by reference), while `start` parameter changes to each neighbor

**Trees & Tries** (`trees+tries.py`):
- **Tree Properties**:
  - Acyclic connected graph with hierarchical structure
  - **Root node**: Top node with no parent, starting point for traversal
  - **Child nodes**: Nodes directly connected below a parent
  - **Siblings**: Nodes with the same parent
  - **Leaf nodes**: Nodes with no children (terminal nodes)
  - **Height**: Length of longest path from root to leaf
  - **Depth**: Length of path from root to specific node
  - **Degree**: Number of children a node has

- **Binary Trees**:
  - Each node has at most two children (left and right)
  - Used for expression trees, decision trees, hierarchical data

- **Binary Search Trees (BSTs)**:
  - Left child < parent node < right child (ordering property)
  - Average time complexity: O(log n) for search, insert, delete (balanced trees)
  - Used in databases, indexing systems requiring fast lookups

- **Tries (Prefix Trees)**:
  - Tree structure optimized for storing and retrieving strings
  - Each node represents a single character
  - Path from root to leaf represents complete string
  - Exploits common prefixes to optimize space and search time
  - `TrieNode` class with `children` dictionary and `is_end_of_word` flag
  - `insert()`: Traverse/create nodes for each character, mark end
  - `search()`: Traverse nodes following characters, check end flag
  - Use cases: Autocomplete, spell checkers, IP routing

**Priority Queues & Heaps** (`priority-queues+heaps.py`):
- **Priority Queue (ADT)**:
  - Elements have associated priorities
  - Higher priority elements served before lower priority
  - Use cases: Shortest path algorithms, task scheduling, traffic simulation, data compression

- **Heap Implementation**:
  - Specialized tree-based structure satisfying heap property
  - **Max-Heap**: Parent ≥ all children (maximum at root)
  - **Min-Heap**: Parent ≤ all children (minimum at root)
  - Root always contains highest/lowest priority element for O(1) access
  
- **Array-Based Heap**:
  - Implemented as arrays for efficient parent/child access
  - For node at index `i`:
    - Left child: `2i + 1`
    - Right child: `2i + 2`
    - Parent: `(i - 1) // 2`

- **Python's `heapq` Module**:
  - Efficient min-heap implementation operating on lists
  - `heappush(heap, item)`: Add element maintaining heap property
  - `heappop(heap)`: Remove and return smallest element
  - `heappushpop(heap, item)`: Push then pop in single efficient operation
  - `heapify(list)`: Transform existing list into heap in-place
  - **Max-heap trick**: Invert values with `-1` multiplication
  - **Priority tuples**: `(priority, value)` where lower number = higher priority
  - Efficient space/time due to array representation

### Key Concepts Learned
- **Graph Theory**: Modeling complex relationships and networks
- **Traversal Strategies**: BFS for shortest paths, DFS for exhaustive search
- **Data Structure Trade-offs**: Matrix vs list, time vs space complexity
- **Recursive Thinking**: Understanding shared state vs changing parameters in DFS
- **Tree Hierarchies**: Representing parent-child relationships efficiently
- **String Optimization**: Tries for prefix-based operations
- **Priority Management**: Heaps for efficient min/max element access
- **Array-Based Trees**: Index calculations for parent/child navigation
- **Algorithm Selection**: Choosing right structure based on problem requirements

**Focus Areas:** Graph representations, BFS/DFS traversal, tree structures, heap operations, space/time trade-offs

---

## Day 11: Data Validation & Serialization - Dataclasses, JSON & Pydantic 📋

**Date:** February 2, 2026

Explored modern Python tools for data validation, serialization, and structured data management. Focused on dataclasses for reducing boilerplate, JSON for data interchange, and Pydantic for robust validation and type safety.

### Core Concepts

**Dataclasses** (`data_class.py`):
- **`@dataclass` Decorator**: Automatically generates special methods (`__init__`, `__repr__`, `__eq__`)
- **Purpose**: Simplifies classes primarily used for storing data
- **Reduces Boilerplate**: No manual `__init__` method needed
- **Type Annotations**: Required for each field to define structure
- **Default Values**: Use `= None` or other defaults for optional fields
- **`field()` Function**: Advanced configuration for mutable defaults
  - `field(default_factory=list)`: Creates new empty list for each instance
  - Prevents shared mutable default problem
  - Accepts additional arguments for customization (default, init, repr, compare)
- **Use Cases**: Configuration objects, DTOs (Data Transfer Objects), simple data containers
- **Benefits**: Less code, automatic method generation, clear data structure definition

**JSON Serialization** (`json.py`):
- **`json` Module**: Built-in Python library for JSON handling
- **File Operations**:
  - `json.dump(data, file)`: Write Python object to JSON file
  - `json.load(file)`: Read JSON file into Python object
- **String Operations**:
  - `json.dumps(data)`: Convert Python object to JSON string
  - `json.loads(string)`: Convert JSON string to Python object
- **Key Distinction**: `dump`/`load` work with files, `dumps`/`loads` work with strings
- **Use Cases**: API data exchange, configuration files, data persistence
- **Data Types**: Supports dict, list, str, int, float, bool, None
- **Limitations**: Cannot serialize complex types (datetime, custom classes) without custom encoders

**Pydantic Basics** (`what_is_it.py`):
- **Purpose**: Data validation library using type annotations
- **`BaseModel`**: Base class for creating validated data models
- **Type Annotations**: Define expected structure and types
- **Automatic Validation**: Validates data when creating instances
- **`ValidationError`**: Raised when data doesn't match schema
- **Default Values**: Support for `None` defaults and empty collections
- **Union Types**: `datetime | None` syntax for optional fields
- **Use Cases**: API request/response validation, configuration management, data parsing
- **Benefits**: Runtime validation, clear error messages, automatic type conversion

**Pydantic BaseModel Advanced** (`basemodel.py`):
- **`Field()` Function**: Enhanced field configuration with metadata
  - `Field(...)`: Marks field as required (no default)
  - `Field(None)`: Optional field with default
  - `Field([])`: Default value for collections
  - Parameters: `title`, `description` for documentation
- **`ConfigDict`**: Model-wide configuration
  - `extra="allow"`: Permits additional fields not defined in model
  - `extra="forbid"`: Rejects unknown fields
  - `extra="ignore"`: Silently ignores unknown fields
- **Special Attributes** (commented examples):
  - `__class_vars__`: Class variable definitions
  - `__private_attributes__`: Private attribute definitions  
  - `__signature__`: Model's `__init__` signature
  - `__pydantic_complete__`: Model definition completeness flag
  - `__pydantic_core_schema__`: Core schema definition
  - `__pydantic_custom_init__`: Custom initialization indicator
  - `__pydantic_decorators__`: Metadata for validators and decorators
  - `__pydantic_generic_metadata__`: Generic model metadata
- **Union Types**: Modern `|` syntax for type unions (Python 3.10+)
- **Type Safety**: Catches type errors at runtime before they cause issues
- **Documentation**: Fields self-document with descriptions and constraints

### Key Concepts Learned
- **Boilerplate Reduction**: Dataclasses eliminate repetitive `__init__` code
- **Data Validation**: Pydantic ensures data integrity with type checking
- **Serialization**: JSON module bridges Python objects and text format
- **Field Configuration**: `field()` and `Field()` for advanced defaults and metadata
- **Type Annotations**: Central to modern Python data structures
- **Default Factory Pattern**: Avoiding mutable default arguments
- **Configuration Objects**: Different approaches (dataclass vs Pydantic) for different needs
- **API Development**: Pydantic's role in FastAPI and data validation
- **Trade-offs**: Dataclasses for simplicity, Pydantic for validation
- **Runtime Type Checking**: Moving beyond static type hints to enforced validation

**Focus Areas:** Data validation, type annotations, JSON serialization, dataclass decorators, Pydantic models

---

## Day 13: FastAPI - Modern Web Framework & Async Programming 🚀

**Date:** February 4, 2026

Began exploring FastAPI, a modern, high-performance web framework for building APIs with Python. Focused on understanding async programming, type hints in web contexts, and the fundamentals of building fast, production-ready APIs.

### Core Concepts

**FastAPI Basics** (`what_is_it.py`):
- **What is FastAPI**: Modern, fast web framework for building APIs with Python based on standard type hints
- **Built on Starlette**: Uses Starlette for web components, providing high-performance asynchronous capabilities
- **Automatic Documentation**: Interactive API docs generated automatically from type hints
- **Pydantic Integration**: Request and response validation through Pydantic models
- **Type Hints in Web Context**:
  - Path parameters with type annotations: `@app.get("/items/{item_id}")`
  - Query parameters with defaults: `q: str = None`
  - Return type annotations for automatic response validation
  - Union types for flexible parameter handling: `int | float`
  - Optional parameters using `typing.Optional[int]` (equivalent to `Union[int, None]`)

- **Async Functions**: 
  - `async def` enables handling multiple requests concurrently
  - `await` keyword for asynchronous I/O operations
  - Suitable for high-performance applications
  - **Important**: Ensure I/O operations within async functions are also async to fully benefit

- **Running FastAPI**:
  - Use Uvicorn ASGI server: `fastapi dev {file_name}:app --reload`
  - `--reload` enables auto-restart on code changes (dev mode)
  - Example: `fastapi dev what_is_it:app --reload`

- **Endpoint Definition**:
  - `@app.get("/")`: Defines GET endpoint for retrieving data
  - Path operations return dictionaries automatically serialized to JSON
  - Route parameters extracted from URL path
  - Query parameters from URL query string

**Type Hints Deep Dive**:
- **Union Types**: `int | float` for multiple accepted types (Python 3.10+)
- **Optional Types**: `typing.Optional[int] = None` (shorthand for `Union[int, None]`)
- **Return Type Annotations**: `-> str` defines function return type
- **Class Attributes**: Type hints for instance variables in `__init__`
- **Benefits**: 
  - Automatic validation by FastAPI/Pydantic
  - Better IDE support and autocomplete
  - Self-documenting code
  - Automatic API schema generation

**Concurrency & Parallelism** (`concurrency+parallelism.py`):
- **Concurrency vs Parallelism**:
  - **Concurrency**: Handling multiple tasks at the same time (task switching)
  - **Parallelism**: Executing multiple tasks simultaneously (true parallel execution)

- **When to Use Each**:
  - **Concurrency**: I/O-bound tasks (database queries, API calls, file operations)
  - **Parallelism**: CPU-bound tasks (intensive computation, data processing)

- **Async/Await Pattern**:
  - `asyncio.sleep(delay)`: Non-blocking delay for I/O simulation
  - `asyncio.gather(*tasks)`: Run multiple async tasks concurrently
  - `asyncio.run(main())`: Entry point for async programs
  - Tasks start simultaneously and complete based on their delay
  - Efficient for I/O-bound operations without blocking main thread

- **ProcessPoolExecutor for Parallelism**:
  - `concurrent.futures.ProcessPoolExecutor`: Execute tasks across multiple CPU cores
  - `executor.submit(function, args)`: Submit CPU-bound tasks for parallel execution
  - `task.result()`: Wait for task completion and get result
  - True parallel execution for CPU-intensive workloads
  - Output appears after all tasks complete (not interleaved like async)

- **Key Differences**:
  - **Async (Concurrency)**: Single thread, task switching, faster for I/O
  - **Multiprocessing (Parallelism)**: Multiple processes, true parallel, faster for CPU tasks
  - FastAPI leverages async for handling many simultaneous requests efficiently

### Practical Examples

**Simple API Endpoints**:
```python
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
```

**Concurrent I/O Tasks**:
```python
async def fake_io_task(task_id: int, delay: float):
    await asyncio.sleep(delay)
    print(f"Task {task_id} completed after {delay} seconds")

# Tasks run concurrently, complete in order of delay
await asyncio.gather(
    fake_io_task(1, 2),
    fake_io_task(2, 1),
    fake_io_task(3, 3)
)
```

**Parallel CPU Tasks**:
```python
with ProcessPoolExecutor() as executor:
    tasks = [
        executor.submit(cpu_bound_task, 1, 10**6),
        executor.submit(cpu_bound_task, 2, 10**6),
    ]
    for task in tasks:
        task.result()  # Wait for completion
```

### Key Concepts Learned
- **Modern Python Web Development**: FastAPI as production-ready framework
- **Type-Driven Development**: Using type hints for validation and documentation
- **Async Programming**: Non-blocking I/O for concurrent request handling
- **Performance Optimization**: Choosing between concurrency and parallelism
- **ASGI Servers**: Uvicorn for running async Python web applications
- **API Design Patterns**: Path parameters, query parameters, automatic JSON serialization
- **Concurrent Execution Models**: Event loop vs multiprocessing
- **I/O vs CPU Bound**: Identifying task types and appropriate handling strategies

**Focus Areas:** FastAPI basics, async/await patterns, type hints in APIs, concurrency models, parallelism with multiprocessing

## Day 14: Advanced Algorithms & Data Traversal

### Neetcode
- **Group Anagrams** (`Neetcode/group-anagrams.py`): Grouping words by anagram similarity using hash maps
- **Is Palindrome** (`Neetcode/is_palindrome.py`): Checking if a string is a palindrome efficiently

### Recursive Data Traversal
- **Factorial** (`Recursive Data Traversal/factorial.py`): Recursive calculation of factorial
- **Fibonacci** (`Recursive Data Traversal/fibonacci.py`): Recursive and iterative Fibonacci sequence generation
- **Intro** (`Recursive Data Traversal/intro.py`): Introduction to recursive traversal concepts
- **Quicksort** (`Recursive Data Traversal/quicksort.py`): Recursive quicksort algorithm implementation
- **Walking HCL** (`Recursive Data Traversal/walking-hcl.py`): Traversing HCL data structures recursively
- **Walking JSON** (`Recursive Data Traversal/walking-json.py`): Recursive traversal of JSON data
- **Walking YAML** (`Recursive Data Traversal/walking-yaml.py`): Recursive traversal of YAML data

---
## Day 15: Data Structures with NetworkX

### NetworkX
- **Info** (`NetworkX/info.py`): Overview and exploration of NetworkX library features
- **Learning Data Structures with NetworkX** (`NetworkX/learning data structures with nx/data-structs.md`): Applying NetworkX to learn and visualize data structures

---