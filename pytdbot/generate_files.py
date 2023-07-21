if __name__ == "__main__":
    from json import loads
    import utils

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
            return _type

    updates_dec = """    def on_{update_name}(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
    ) -> Callable:
        \"\"\"{description}

        Args:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

        Raises:
            :py:class:`TypeError`
        \"\"\"

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler("{update_name}", func, filters, position)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func, "{update_name}", self, position)
            else:
                func._handler = Handler(func, "{update_name}", filters, position)
            return func

        return decorator

"""

    def updates():
        with open("handlers/updates.py", "w") as f:
            f.write(
                'import pytdbot\n\nfrom .handler import Handler\nfrom typing import Callable\nfrom asyncio import iscoroutinefunction\nfrom logging import getLogger\n\nlogger = getLogger(__name__)\n\n\nclass Updates:\n    """Auto generated TDLib updates"""\n\n'
            )
            for k, v in data["updates"].items():
                f.write(
                    updates_dec.format(
                        update_name=k,
                        description=utils.escape_markdown(v["description"]),
                    )
                )

    def functions():
        with open("methods/tdlibfunctions.py", "w") as f:
            f.write(
                'from ..types import Result\n\nclass TDLibFunctions:\n    """Auto generated TDLib functions"""\n\n'
            )
            for k, v in data["functions"].items():
                # if k.startswith("test"):
                #     continue
                f.write(f"    async def {k}(self")
                if p := getP(v["args"]):
                    f.write(f",{p}" + ") -> Result:\n")
                else:
                    f.write(") -> Result:\n")

                f.write(f'        """{utils.escape_markdown(v["description"])}\n\n')

                if v["args"]:
                    f.write(f"        Args:\n")
                    params = dict(
                        sorted(v["args"].items(), key=lambda x: x[1]["is_optional"])
                    )

                    for _k, _v in params.items():
                        if not _v["is_optional"]:
                            f.write(
                                f"            {_k} (``{getType(_v['type'])}``):\n                {utils.escape_markdown(_v['description'])}\n\n"
                            )
                        else:
                            f.write(
                                f"            {_k} (``{getType(_v['type'])}``, *optional*):\n                {utils.escape_markdown(_v['description'])}\n\n"
                            )
                f.write(
                    '\n        Returns:\n            :class:`~pytdbot.types.Result` (``{}``)\n        """\n\n'.format(
                        v["type"]
                    )
                )
                f.write(f"        data = {{'@type': '{k}',")
                for k in v["args"]:
                    f.write(f" '{k}': {k},")
                f.write("}\n\n        return await self.invoke(data)\n\n")

    updates()
    functions()
