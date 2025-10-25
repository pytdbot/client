import json
import keyword

indent = "    "
bound_methods_class = {
    "Message": "MessageBoundMethods",
    "File": "FileBoundMethods",
    "RemoteFile": "FileBoundMethods",
    "UpdateNewCallbackQuery": "CallbackQueryBoundMethods",
    "MessageSender": "MessageSenderBoundMethods",
}


def escape_quotes(text: str):
    return "".join(
        "\\" + c if c in r"\_*[]()~`>#+-=|{}.!" else c for c in text
    ).replace('"', '\\"')


def to_camel_case(input_str: str, delimiter: str = ".", is_class: bool = True) -> str:
    if not input_str:
        return ""

    parts = input_str.split(delimiter)
    camel_case_str = ""

    for i, part in enumerate(parts):
        if i > 0:
            camel_case_str += part[0].upper() + part[1:]
        else:
            camel_case_str += part

    if camel_case_str:
        camel_case_str = (
            camel_case_str[0].upper() if is_class else camel_case_str[0].lower()
        ) + camel_case_str[1:]

    return camel_case_str


arg_types = {
    "double": "float",
    "string": "str",
    "secureString": "str",
    "int32": "int",
    "int53": "int",
    "int64": "int",
    "int256": "int",
    "bytes": "bytes",
    "secureBytes": "bytes",
    "Bool": "bool",
    "Object": "dict",
    "Function": "dict",
    "#": "int",
}


def getArgTypePython(
    type_name: str, is_function: bool = False, is_docstring: bool = False
):
    if type_name in arg_types:
        if is_docstring:
            return f":class:`{arg_types[type_name]}`"

        return arg_types[type_name]

    if "?" in type_name:
        return getArgTypePython(type_name.split("?")[-1], is_function, is_docstring)

    if type_name.startswith("("):
        type_name = type_name.strip("()")
        kind, inner = type_name.split(" ", 1)
        if kind == "vector":
            return f"List[{getArgTypePython(inner, is_function, is_docstring)}]"
        raise ValueError(f"Unknown data type: {kind}/{inner}")

    if type_name.startswith("vector<") and type_name.endswith(">"):
        inner = type_name[7:-1]
        return f"List[{getArgTypePython(inner, is_function, is_docstring)}]"

    class_name = to_camel_case(type_name, is_class=True)

    if is_function:
        if is_docstring:
            return f":class:`~pytdbot.types.{class_name}`"
        return f'"pytdbot.types.{class_name}"'

    return class_name


def generate_arg_value(arg_type, arg_name):
    if arg_type == "int":
        arg_value = f"int({arg_name})"
    elif arg_type == "float":
        arg_value = f"float({arg_name})"
    elif arg_type == "bool":
        arg_value = f"bool({arg_name})"
    elif arg_type.startswith("List[") or arg_type == "list":
        arg_value = f"{arg_name} or []"
    else:
        arg_value = arg_name

    return arg_value


def generate_arg_default(arg_type):
    if arg_type == "int":
        arg_value = "0"
    elif arg_type == "str":
        arg_value = '""'
    elif arg_type == "float":
        arg_value = "0.0"
    elif arg_type == "bytes":
        arg_value = 'b""'
    elif arg_type == "bool":
        arg_value = "False"
    else:
        arg_value = "None"

    return arg_value


def generate_args_def(args, is_function: bool = False):
    args_list = ["self"]
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        arg_type = getArgTypePython(arg_data["type"], is_function)

        args_list.append(f"{arg_name}: {arg_type} = {generate_arg_default(arg_type)}")

    return ", ".join(args_list)


def generate_union_types(arg_type, arg_type_name, classes, noneable=True):
    unions = [arg_type]

    if (
        arg_type_name in classes
    ):  # The arg type is a class which has subclasses and we need to include them
        unions.pop(0)

        for type_name in classes[arg_type_name]["types"]:
            unions.append(to_camel_case(type_name, is_class=True))

    if noneable:
        unions.append("None")

    return f"Union[{', '.join(unions)}]"


def generate_self_args(args, classes):
    args_list = []
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        arg_type = getArgTypePython(arg_data["type"])
        arg_value = generate_arg_value(arg_type, arg_name)
        if arg_value == arg_name:  # a.k.a field can be None
            arg_type = generate_union_types(arg_type, arg_data["type"], classes)

        args_list.append(
            f'self.{arg_name}: {arg_type} = {arg_value}\n{indent * 2}r"""{escape_quotes(arg_data["description"])}"""'
        )
    if not args_list:
        return "pass"
    return f"\n{indent * 2}".join(args_list)


def generate_to_dict_return(args):
    args_list = ['"@type": self.getType()']
    for arg_name, _ in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"
        args_list.append(f'"{arg_name}": self.{arg_name}')

    return ", ".join(args_list)


def generate_from_dict_kwargs(args):
    args_list = []
    for arg_name, arg_data in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"

        arg_type = getArgTypePython(arg_data["type"])

        if arg_type == "bytes":
            args_list.append(
                f'data_class.{arg_name} = b64decode(data.get("{arg_name}", b""))'
            )
        elif arg_type == "int":  # Some values are int but in string format
            args_list.append(f'data_class.{arg_name} = int(data.get("{arg_name}", 0))')
        else:
            args_list.append(
                f'data_class.{arg_name} = data.get("{arg_name}", {generate_arg_default(arg_type)})'
            )

    return "; ".join(args_list)


def generate_function_invoke_args(args):
    args_list = []
    for arg_name, _ in args.items():
        if arg_name in keyword.kwlist:
            arg_name += "_"
        args_list.append(f'"{arg_name}": {arg_name}')

    return ", ".join(args_list)


def generate_function_docstring_args(function_data):
    if not function_data["args"]:
        return ""
    args_list = []
    for arg_name, arg_data in function_data["args"].items():
        args_list.append(
            f"{indent * 3}{arg_name} ({getArgTypePython(arg_data['type'], True, True)}):\n{indent * 4 + escape_quotes(arg_data['description'])}"
        )
    return f"\n{indent * 2}Parameters:\n" + "\n\n".join(args_list) + "\n"


def generate_inherited_class(class_name, type_data, classes):
    inherited = ["TlObject"]
    if type_data["type"] in classes:
        inherited.append(to_camel_case(type_data["type"], is_class=True))

    if class_name in bound_methods_class:
        inherited.append(bound_methods_class[class_name])
    return ", ".join(inherited)


class_template = """class {class_name}{inherited_class}:
    r\"\"\"{docstring}\"\"\"

    pass"""


def generate_classes(f, classes):
    for class_name in classes.keys():
        class_name = to_camel_case(class_name, is_class=True)

        f.write(
            class_template.format(
                class_name=class_name,
                inherited_class=""
                if class_name not in bound_methods_class
                else f"({bound_methods_class[class_name]})",
                docstring=escape_quotes(classes[class_name]["description"]),
            )
            + "\n\n"
        )


types_template = """class {class_name}({inherited_class}):
    r\"\"\"{docstring}
{docstring_args}
    \"\"\"

    def __init__({init_args}) -> None:
        {self_args}

    def __str__(self):
        return str(pytdbot.utils.obj_to_json(self, indent=4))

    @classmethod
    def getType(self) -> Literal["{type_name}"]:
        return "{type_name}"

    @classmethod
    def getClass(self) -> Literal["{class_type_name}"]:
        return "{class_type_name}"

    def to_dict(self) -> dict:
        return {{{to_dict_return}}}

    @classmethod
    def from_dict(cls, data: dict) -> Union["{class_name}", None]:
        if data:
            data_class = cls()
            {from_dict_kwargs}

        return data_class"""


def generate_types(f, types, updates, classes):
    def gen(t):
        for type_name, type_data in t.items():
            args_def = generate_args_def(type_data["args"])
            self_args = generate_self_args(type_data["args"], classes)
            to_return_dict = generate_to_dict_return(type_data["args"])
            from_dict_kwargs = generate_from_dict_kwargs(type_data["args"])
            class_name = to_camel_case(type_name, is_class=True)

            f.write(
                types_template.format(
                    class_name=class_name,
                    inherited_class=generate_inherited_class(
                        class_name, type_data, classes
                    ),
                    class_type_name=type_data["type"],
                    docstring=escape_quotes(type_data["description"]),
                    docstring_args=generate_function_docstring_args(type_data),
                    init_args=args_def,
                    self_args=self_args,
                    type_name=type_name,
                    to_dict_return=to_return_dict,
                    from_dict_kwargs=from_dict_kwargs,
                )
                + "\n\n"
            )

    gen(types)
    gen(updates)


functions_template = """async def {function_name}({function_args}) -> Union["pytdbot.types.Error", "pytdbot.types.{return_type}"]:
        r\"\"\"{docstring}
{docstring_args}
        Returns:
            :class:`~pytdbot.types.{return_type}`
        \"\"\"

        return await self.invoke({{'@type': '{method_name}', {function_invoke_args}}})"""


def generate_functions(f, types):
    for function_name, function_data in types.items():
        args_def = generate_args_def(function_data["args"], True)
        invoke_args = generate_function_invoke_args(function_data["args"])

        f.write(
            indent
            + functions_template.format(
                function_name=to_camel_case(function_name, is_class=False),
                function_args=args_def,
                return_type=to_camel_case(function_data["type"], is_class=True),
                docstring=escape_quotes(function_data["description"]),
                docstring_args=generate_function_docstring_args(function_data),
                method_name=function_name,
                function_invoke_args=invoke_args,
            )
            + "\n\n"
        )


updates_template = """    def on_{update_name}(
        self: "pytdbot.Client" = None,
        filters: "pytdbot.filters.Filter" = None,
        position: int = None,
        timeout: float = None,
    ) -> Callable:
        r\"\"\"{description}

        Parameters:
            filters (:class:`pytdbot.filters.Filter`, *optional*):
                An update filter

            position (``int``, *optional*):
                The function position in handlers list. Default is ``None`` (append)

            timeout (``float``, *optional*):
                Max execution time for the handler before it timeout. Default is ``None``

        Raises:
            :py:class:`TypeError`
        \"\"\"

        def decorator(func: Callable) -> Callable:
            if hasattr(func, "_handler"):
                return func
            elif isinstance(self, pytdbot.Client):
                if iscoroutinefunction(func):
                    self.add_handler(update_type="{update_name}", func=func, filters=filters, position=position, inner_object=False, timeout=timeout)
                else:
                    raise TypeError("Handler must be async")
            elif isinstance(self, pytdbot.filters.Filter):
                func._handler = Handler(func=func, update_type="{update_name}", filter=self, position=position, inner_object=False, timeout=timeout)
            else:
                func._handler = Handler(func=func, update_type="{update_name}", filter=filters, position=position, inner_object=False, timeout=timeout)
            return func

        return decorator

"""


def generate_updates(f, updates):
    for k, v in updates.items():
        f.write(
            updates_template.format(
                update_name=k,
                description=escape_quotes(v["description"]),
            )
        )


if __name__ == "__main__":
    with open("td_api.json", "r") as f:
        tl_json = json.loads(f.read())

    with open("pytdbot/types/td_types.py", "w") as types_file:
        types_file.write("from typing import Union, Literal, List\n")
        types_file.write("from base64 import b64decode\n")
        types_file.write(
            f"from .bound_methods import {', '.join(set(bound_methods_class.values()))}\n"
        )
        types_file.write("import pytdbot\n\n")
        types_file.write(
            """class TlObject:
    \"\"\"Base class for TL Objects\"\"\"

    def __getitem__(self, item):
        if item == "@type":
            return self.getType()

        return self.__dict__[item]

    def __setitem__(self, item, value):
        self.__dict__[item] = value

    def __bool__(self):
        return not isinstance(self, Error)

    @property
    def is_error(self): # for backward compatibility
        return isinstance(self, Error)

    @property
    def limited_seconds(self):
        if self.is_error and self.code == 429:
            return pytdbot.utils.get_retry_after_time(self.message)
        else:
            return 0

    @classmethod
    def getType(cls):
        raise NotImplementedError

    @classmethod
    def getClass(cls):
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError

    @classmethod
    def from_dict(cls, data: dict):
        raise NotImplementedError\n\n"""
        )

        generate_classes(types_file, tl_json["classes"])
        generate_types(
            types_file, tl_json["types"], tl_json["updates"], tl_json["classes"]
        )

    with open("pytdbot/types/__init__.py", "w") as types_init_file:
        types_names = [
            to_camel_case(name, is_class=True)
            for section in ("classes", "types", "updates")
            for name in tl_json[section].keys()
        ]

        all_classes = (
            '__all__ = ["TlObject", "Plugins", "ServerStats", "ScheduledEvent", "UpdateScheduledEvent", '
            + ", ".join(f'"{name}"' for name in types_names)
            + "]\n\n"
        )
        types_init_file.write(all_classes)

        classes_import = f"from .td_types import TlObject, {', '.join(types_names)}\nfrom .plugins import Plugins\nfrom .tdserver import ServerStats, ScheduledEvent, UpdateScheduledEvent"
        types_init_file.write(classes_import)
        types_init_file.write('\n\nTDLIB_VERSION = "{}"'.format(tl_json["version"]))

    with open("pytdbot/methods/td_functions.py", "w") as functions_file:
        functions_file.write("from typing import Union, List\nimport pytdbot\n\n")

        functions_file.write("class TDLibFunctions:\n")
        functions_file.write(
            f'{indent}"""A class that include all TDLib functions"""\n\n'
        )

        generate_functions(functions_file, tl_json["functions"])

    with open("pytdbot/handlers/td_updates.py", "w") as updates_file:
        updates_file.write(
            'import pytdbot\n\nfrom .handler import Handler\nfrom typing import Callable\nfrom asyncio import iscoroutinefunction\nfrom logging import getLogger\n\nlogger = getLogger(__name__)\n\n\nclass Updates:\n    """Auto generated TDLib updates"""\n\n'
        )

        generate_updates(updates_file, tl_json["updates"])
