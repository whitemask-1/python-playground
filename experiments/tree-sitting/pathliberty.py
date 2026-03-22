from pathlib import Path

def find_python_files(root: str) -> list[Path]:
    return list(Path(root).rglob("*.py"))

files = find_python_files("/Users/p/Documents/Code/env-inspect")
for f in files:
    print(f)
