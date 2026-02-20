# Python Playground

A collection of Python projects, experiments, tools, and explorations. This repo is a sandbox for building things, trying out libraries, solving problems, and experimenting with ideas.

---

## Structure

```
.
├── projects/          Standalone projects with real functionality
├── experiments/       Library explorations and framework experiments
├── algorithms/        Data structures, algorithms, and problem solving
├── concepts/          Python language concepts and patterns
├── tools/             Small utility scripts and one-off tools
└── sandbox/           Ideas, scratch work, and project proposals
```

---

## Projects

Larger, self-contained programs.

| Project | Description |
|---------|-------------|
| [**Daily Bugle**](projects/daily-bugle/) | Multi-source news aggregator with rich terminal UI. Fetches from NY Times, Guardian, NewsAPI, and BBC. Persistent rate limiting and config. |
| [**Movie Tracker**](projects/movie-tracker/) | CLI tool for tracking watched/unwatched movies with ratings, genres, and JSON persistence. |
| [**ISBN Validator**](projects/isbn-validator/) | ISBN-10 and ISBN-13 validation tool. |

## Experiments

Trying out libraries and frameworks.

| Experiment | Description |
|------------|-------------|
| [**Matplotlib 3D**](experiments/matplotlib-3d/) | 3D surface plots, fractal generation (Mandelbulb, Mandelbrot, Burning Ship), and animated visualizations. |
| [**FastAPI**](experiments/fastapi/) | Async web framework exploration, concurrency and parallelism patterns. |
| [**NetworkX**](experiments/networkx/) | Graph data structure visualization and analysis. |
| [**Pydantic**](experiments/pydantic/) | Data validation, serialization, custom types, settings config, and field validators. |

## Algorithms

Data structures, sorting, searching, and competitive programming.

| Area | Contents |
|------|----------|
| [**Data Structures**](algorithms/data-structures/) | Arrays, linked lists, stacks, queues, trees, tries, graphs, heaps, hashmaps. |
| [**Search & Sort**](algorithms/search-and-sort/) | Binary search, divide and conquer. |
| [**Recursion**](algorithms/recursion/) | Factorial, Fibonacci, quicksort, recursive data traversal (JSON, YAML, HCL). |
| [**LeetCode**](algorithms/leetcode/) | Two Sum, Valid Anagram, Contains Duplicate, Group Anagrams, Products Except Self, Valid Sudoku, and more. |

## Concepts

Python language features and patterns, organized by topic.

| Topic | Contents |
|-------|----------|
| [**Fundamentals**](concepts/fundamentals/) | Types, strings, numbers, booleans, conditionals, loops, lists, tuples, dicts, sets, functions, scope, comprehensions, lambdas, dataclasses, JSON. |
| [**OOP**](concepts/oop/) | Classes, objects, methods, attributes, inheritance, polymorphism, abstraction, encapsulation, getters/setters, name mangling, special methods. |
| [**Error Handling**](concepts/error-handling/) | Exceptions, debugging, raise, user config patterns. |

## Tools

Small, standalone utility scripts.

| Tool | Description |
|------|-------------|
| [`caesar-cipher.py`](tools/ceasar-cipher.py) | Caesar cipher encryption/decryption. |
| [`rpg-character.py`](tools/rpg-character.py) | RPG character generator with stats and classes. |
| [`medical-validator.py`](tools/medical-validator.py) | Medical data validation tool. |
| [`pin-extractor.py`](tools/pin-extractor.py) | PIN extraction utility. |

## Sandbox

Ideas and proposals for future projects.

- [Project ideas](sandbox/THEIDEA.md) - Brainstorm for "thinking machines" and tools
- [Chess Remake](sandbox/chess-remake.md) - Terminal chess game proposal
- [Handlr](sandbox/handlr.md) - Text processing tool proposal

---

## Getting Started

```bash
# Clone the repo
git clone <repo-url>
cd python-playground

# Create a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate

# Run any script directly
python projects/daily-bugle/daily_bugle.py
python tools/ceasar-cipher.py
python algorithms/leetcode/two-sum.py
```

Some projects may need additional dependencies (e.g., `matplotlib`, `pydantic`, `fastapi`, `networkx`). Install as needed:

```bash
pip install matplotlib pydantic fastapi networkx rich requests
```
