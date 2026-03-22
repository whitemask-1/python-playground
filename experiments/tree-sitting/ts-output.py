import tree_sitter_python as tspython
from pathlib import Path
from tree_sitter import Parser, Language, Tree

PY_LANG = Language(tspython.language())
python_parser = Parser(PY_LANG)


def parse_py_file(path: Path) -> Tree:
    source = path.read_bytes()
    tree = python_parser.parse(source)
    return tree

def find_python_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.py"))

files = find_python_files("/Users/p/Documents/Code/env-inspect/envinspect")

def walking_py_tree(pytree: Tree):
    py_walker = pytree.root_node.walk()
    print(py_walker.node.id)
    print(py_walker.node.type)
    print(py_walker.node.child_by_field_name("name"))
    print(py_walker.node.start_point)
    print(py_walker.node.end_point)
    print("\n")

for f in files:
    file_tree = parse_py_file(f)
    walking_py_tree(file_tree)
