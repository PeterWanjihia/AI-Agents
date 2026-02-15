from pathlib import Path

def list_directory(path:str):
    root = Path(path)
    for p in  sorted(root.iterdir()):
        return [p.name for p in sorted(root.iterdir())]
    
files = list_directory("/home/moringa/AgentCompute")
print(files)


