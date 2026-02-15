from pathlib import Path

def list_directory(path:str):
    root = Path(path)
    for p in  sorted(root.iterdir()):
        print(p.name)


