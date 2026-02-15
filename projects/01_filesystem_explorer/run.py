from pathlib import Path

ROOT = Path("/home/moringa/AgentCompute").resolve()

def list_directory(path: str = ".", *, limit: int = 200) -> dict:
    target = (ROOT / path).resolve()

    # sandbox rule
    if target != ROOT and ROOT not in target.parents:
        return {
            "ok": False,
            "path": str(target),
            "entries": [],
            "count": 0,
            "truncated": False,
            "error": "Path outside allowed ROOT",
        }

    # clearer errors
    if not target.exists():
        return {
            "ok": False,
            "path": str(target),
            "entries": [],
            "count": 0,
            "truncated": False,
            "error": "Path does not exist",
        }

    if not target.is_dir():
        return {
            "ok": False,
            "path": str(target),
            "entries": [],
            "count": 0,
            "truncated": False,
            "error": "Path is not a directory",
        }

    try:
        entries = []
        truncated = False

        for p in sorted(target.iterdir(), key=lambda x: x.name.lower()):
            entries.append({
                "name": p.name,
                "type": "dir" if p.is_dir() else "file" if p.is_file() else "other",
            })

            if len(entries) >= limit:
                truncated = True
                break

        return {
            "ok": True,
            "path": str(target),
            "entries": entries,
            "count": len(entries),
            "truncated": truncated,
            "error": None,
        }

    except PermissionError:
        return {
            "ok": False,
            "path": str(target),
            "entries": [],
            "count": 0,
            "truncated": False,
            "error": "Permission denied",
        }

    except Exception as e:
        return {
            "ok": False,
            "path": str(target),
            "entries": [],
            "count": 0,
            "truncated": False,
            "error": f"{type(e).__name__}: {e}",
        }


    
if __name__ == "__main__":
    obs = list_directory(".")
    print(obs)

    
