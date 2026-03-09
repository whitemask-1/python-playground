from pathlib import Path
import shutil

EXTENSION_MAP = {
        "images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg", ".heic"],
        "documents": [".pdf", ".docx", ".doc", ".txt", ".md", ".epub", ".pages"],
        "spreadsheets": [".xlsx", ".xls", ".csv"],
        "code": [".py", ".js", ".ts", ".sh", ".json", ".yaml", ".yml", ".toml"],
        "archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
        "video": [".mp4", ".mov", ".mkv", ".avi"],
        "audio": [".mp3", ".wav", ".flac", ".m4a"],
        "installers": [".dmg", ".pkg", ".exe"],
}

def get_category(extension: str) -> str:
    """Return the category for a given file extension"""
    ext = extension.lower()
    for category, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return category
    return "misc"

def sort_downloads():
    downloads = Path.home() / "Downloads"

    files = [f for f in downloads.iterdir() if f.is_file()]

    for file in files:
        category = get_category(file.suffix)

        target_dir = downloads / category
        target_dir.mkdir(exist_ok=True)

        target_path = target_dir / file.name
        if target_path.exists():
            timestamp = int(file.stat().st_mtime)
            target_path = target_dir / f"{file.stem}_{timestamp}{file.suffix}"

        shutil.move(str(file), str(target_path))
        print(f" {file.name} -> {category}/")

    print(f"\nDone. Sorted {len(files)} files.")

if __name__ == "__main__":
    sort_downloads()
