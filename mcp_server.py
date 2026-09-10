import sys
import json
from client import EGraphCongruenceClosure

eg = EGraphCongruenceClosure()

def handle_call(name, arguments):
    if name == "union":
        eg.union(arguments["x"], arguments["y"])
        return {"status": "ok"}
    elif name == "check_equiv":
        eq = (eg.find(arguments["x"]) == eg.find(arguments["y"]))
        return {"equivalent": eq}
    return {"error": f"Unknown tool: {name}"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            res = handle_call(req.get("name"), req.get("arguments", {}))
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
