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