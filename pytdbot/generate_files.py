from json import loads

with open("td_api.json") as f:
    data = loads(f.read())


def getP(params: dict):
    nullable = []
    non = []
    for k, v in params.items():
        name, _type = k, v["type"]
        param = ""

        if _type == "Bool":
            param = f"{name}: bool"
        elif _type.startswith("int"):
            param = f"{name}: int"
        elif _type == "bytes":
            param = f"{name}: bytes"
        elif _type.startswith("vector"):
            param = f"{name}: list"
        elif _type == "string":
            param = f"{name}: str"
        elif _type == "double":
            param = f"{name}: float"
        else:
            param = f"{name}: dict"

        if v["is_optional"]:
            param += " = None"
            nullable.append(param)
        else:
            non.append(param)
    if non or nullable:
        return ", ".join(non + nullable)


def getType(_type):
    if _type == "Bool":
        return "bool"
    elif _type.startswith("int"):
        return "int"
    elif _type == "bytes":
        return "bytes"
    elif _type.startswith("vector"):
        return "list"
    elif _type == "string":
        return "str"
    elif _type == "double":
        return "float"
    else:
        return "dict"


def updates():
    with open("handlers/updates.py", "w") as f:
        f.write(
            'from .handler import Handler\nfrom typing import Callable\nfrom asyncio import iscoroutinefunction\nfrom logging import getLogger\nimport pytdbot\n\nlogger = getLogger(__name__)\n\n\nclass Updates:\n    """Auto generated tdlib updates"""\n\n'
        )
        for k, v in data["updates"].items():
            f.write(
                '    def on_{update_name}(\n        self: "pytdbot.Client" = None,\n        filters: "pytdbot.filters.Filter" = None,\n        position: int = None,\n    ) -> Callable:\n        """{description}\n\n        Args:\n            filters (:class:`pytdbot.filters.Filter`, optional): An update filter.\n            position (``int``, optional): The function position in handlers list. Defaults to None (append).\n\n        Raises:\n            TypeError\n        """\n\n        def decorator(func: Callable) -> Callable:\n            if hasattr(func, "_handler"):\n                return func\n            elif isinstance(self, pytdbot.Client):\n                if iscoroutinefunction(func):\n                    self.add_handler(\n                        "{update_name}", func, filters, position\n                    )\n                else:\n                    logger.warn(\n                        \'Function "{{}}" is not a coroutine function\'.format(func)\n                    )\n            else:\n                func._handler = Handler(\n                    func, "{update_name}", filters, position\n                )\n            return func\n        return decorator\n\n'.format(
                    update_name=k, description=v["description"]
                )
            )


def functions():
    with open("methods/tdlibfunctions.py", "w") as f:
        f.write(
            'from ..types import Response\n\nclass TDLibFunctions:\n    """Auto generated tdlib functions"""\n\n'
        )
        for k, v in data["functions"].items():
            if k.startswith("test"):
                continue
            f.write(f"    async def {k}(self")
            if p := getP(v["args"]):
                f.write(f",{p}" + ", timeout: float = None) -> Response:\n")
            else:
                f.write(", timeout: float = None) -> Response:\n")

            f.write(f'        """{v["description"]}\n\n')

            if v["args"]:
                f.write(f"        Args:\n")
                params = dict(
                    sorted(v["args"].items(), key=lambda x: x[1]["is_optional"])
                )

                for _k, _v in params.items():
                    if not _v["is_optional"]:
                        f.write(
                            f"            {_k} (``{getType(_v['type'])}``):\n                {_v['description']}\n\n"
                        )
                    else:
                        f.write(
                            f"            {_k} (``{getType(_v['type'])}``, optional):\n                {_v['description']}\n\n"
                        )
            f.write(
                '\n        Returns:\n            :class:`~pytdbot.types.Response`\n        """\n\n'
            )
            f.write(f"        data = {{'@type': '{k}',")
            for k in v["args"]:
                f.write(f" '{k}': {k},")
            f.write("}\n\n        return await self.invoke(data, timeout=timeout)\n\n")


updates()
functions()
