import json
def fixed_json(s):
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        fixed = s.replace("\n", "\\n").replace("\t", "\\t")
        return json.loads(fixed)