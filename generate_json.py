import json
import sys
import re
from pathlib import Path

optional_tags = ("; may be null", "; pass null", "; may be empty", "If non-empty,")


def is_optional(description):
    return any(tag in description for tag in optional_tags)


def main():
    if len(sys.argv) != 3:
        print("Usage: generate_json.py <tdlib_version> <tdlib_commit_hash>")
        exit(1)

    data = {
        "name": "Auto-generated JSON TDLib API for Pytdbot ~ https://github.com/pytdbot/client",
        "version": sys.argv[1],
        "commit_hash": sys.argv[2],
        "classes": {},
        "types": {},
        "updates": {},
        "functions": {},
    }
    params = {}

    start = False
    is_functions = False

    description = ""

    class_regex = re.compile(
        r"//@class\s(?P<name>.*)\s@description\s(?P<description>.*)"
    )
    parameter_regex = re.compile(r"@(.*?)\s+([^@]+)")
    end_param_regex = re.compile(r"(?P<name>\w+):(?P<type>[<\w>]+)")
    end_regex = re.compile(r"^(?P<name>.*?)\s(?P<params>.*)=\s(?P<type>\w+);$")

    tl = Path("td_api.tl").read_text().replace("\n//-", " ")

    for line in tl.splitlines():
        if "--functions--" in line:
            is_functions = True
            continue

        if line.startswith("//"):
            start = True

        if line != "" and start:
            if _class := class_regex.match(line):
                data["classes"][_class.group("name").strip()] = {
                    "description": _class.group("description").strip(),
                    "types": [],
                    "functions": [],
                }
            elif _param := parameter_regex.findall(line):
                for name, _description in _param:
                    if name.strip() == "description":
                        description = _description.strip()
                    else:
                        params[name.replace("param_", "").strip()] = (
                            _description.strip()
                        )
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

                json_name = _end.group("name").strip()
                if is_functions:
                    data["functions"][json_name] = _data
                    if _data["type"] in data["classes"]:
                        data["classes"][_data["type"]]["functions"].append(json_name)
                elif json_name.startswith("update"):
                    data["updates"][json_name] = _data
                    if _data["type"] in data["classes"]:
                        data["classes"][_data["type"]]["types"].append(json_name)
                else:
                    data["types"][json_name] = _data
                    if _data["type"] in data["classes"]:
                        data["classes"][_data["type"]]["types"].append(json_name)

                params = {}
                description = ""

    with open("td_api.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(data, indent=4))
        print(
            "Classes: {}\nTypes: {}\nFunctions: {}\nUpdates: {}".format(
                len(data["classes"]),
                len(data["types"]),
                len(data["functions"]),
                len(data["updates"]),
            )
        )


if __name__ == "__main__":
    main()
