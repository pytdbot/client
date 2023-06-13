from json import dumps
from sys import argv
from re import compile
from pathlib import Path

if __name__ == "__main__":
    if len(argv) != 3:
        print("Usage: generate_json.py <TDLib_version> <Last_TDLib_commit_hash>")
        exit(1)

    data = {
        "name": "Auto-generated JSON TDLib API for Pytdbot ~ https://github.com/pytdbot/client",
        "version": argv[1],
        "commit_hash": argv[2],
        "classes": {},
        "types": {},
        "updates": {},
        "functions": {},
    }
    params = {}
    start = False
    is_functions = False
    description = ""
    class_regex = compile(r"//@class\s(?P<name>.*)\s@description\s(?P<description>.*)")
    description_regex = compile(r"//@description\s(?P<description>.*)$")
    parameter_regex = compile(r"@(.*?)\s+([^@]+)")
    end_param_regex = compile(r"(?P<name>\w+):(?P<type>[<\w>]+)")
    end_regex = compile(r"^(?P<name>.*?)\s(?P<params>.*)=\s(?P<type>\w+);$")
    tl = Path("td_api.tl").read_text().replace("\n//-", " ")

    def is_optional(d):
        return (
            "; may be null" in d
            or "; pass null" in d
            or "; may be empty" in d
            or "If non-empty," in d
        )

    for line in tl.split("\n"):
        if "--functions--" in line:
            is_functions = True
            continue

        if line.startswith("//"):
            start = True

        if line != "" and start:
            if _class := class_regex.match(line):
                data["classes"][_class.group("name").strip()] = _class.group(
                    "description"
                ).strip()
            elif _param := parameter_regex.findall(line):
                for name, _description in _param:
                    if name.strip() == "description":
                        description = _description.strip()
                    else:
                        params[
                            name.replace("param_", "").strip()
                        ] = _description.strip()
            elif _end := end_regex.match(line):
                _data = {
                    "description": description,
                    "args": {},
                    "type": _end.group("type").strip(),
                }

                for keyv in end_param_regex.finditer(_end.group("params")):
                    k, v = keyv.group("name").strip(), keyv.group("type").strip()
                    _data["args"][k] = {
                        "description": params[k],
                        "is_optional": is_optional(params[k]),
                        "type": v,
                    }
                if is_functions:
                    data["functions"][_end.group("name").strip()] = _data
                elif _end.group("name").strip().startswith("update"):
                    data["updates"][_end.group("name").strip()] = _data
                else:
                    data["types"][_end.group("name").strip()] = _data
                params = {}
                description = ""

    with open("td_api.json", "w") as f:
        f.write(dumps(data, indent=4))
        print(
            "Classes: {}\nTypes: {}\nFunctions: {}\nUpdates: {}".format(
                len(data["classes"]),
                len(data["types"]),
                len(data["functions"]),
                len(data["updates"]),
            )
        )
