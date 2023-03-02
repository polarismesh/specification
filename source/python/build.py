import os
import re
import typing

import pkg_resources


def run_protoc(
    output_dir: str,
    proto_includes: typing.List[str],
    input_files: str = str,
):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    proto_includes = [pkg_resources.resource_filename("grpc_tools", "_proto")] + proto_includes

    proto_include_list = [f"--proto_path={proto_include}" for proto_include in proto_includes]

    command_arguments = (
        [
            "grpc_tools.protoc",
            f"--python_out={output_dir}",
            f"--grpc_python_out={output_dir}",
            f"--pyi_out={output_dir}",
        ]
        + proto_include_list
        + [f"--proto_path={input_files}"]
    )

    command = "python -m " + " ".join(command_arguments)

    """ run protoc any error will be raised """
    try:
        os.system(command)
    except Exception as e:
        print(e)
        raise e


def run():
    current = os.getcwd()
    output_dir = f"{current}/source/python/src/polarismesh_specification/api/v1"
    api_definition_path = f"{current}/api/v1"
    api_definitions = ["model", "service_manage", "traffic_manage", "fault_tolerance", "config_manage", "security"]
    api_definition_relations = {
        "service_manage": ["model", "traffic_manage", "fault_tolerance", "config_manage", "security"],
        "traffic_manage": ["model"],
        "fault_tolerance": ["model"],
        "config_manage": ["model"],
    }
    api_default_include = ["source/protoc/protoc-linux-x86_64/include"]

    for api_item in api_definitions:
        api_item_path = f"{api_definition_path}/{api_item}"
        """ all .proto files in api_item_path """
        files = [file for file in os.listdir(api_item_path) if file.endswith(".proto")]
        files_str = " ".join(files)
        """ get api_definition_relations[api_item] list + api_definition_path """
        relations = [f"{api_definition_path}/{relation}" for relation in api_definition_relations.get(api_item, [])]
        all_proto_paths = api_default_include + relations
        run_protoc(f"{output_dir}/{api_item}", all_proto_paths, f"{api_item_path} {files_str}")

    """ generate __init__.py and __init__.pyi """
    for api_item in api_definitions:
        output_path = f"{output_dir}/{api_item}"
        files = [file for file in os.listdir(output_path) if file.endswith(".py")]
        files = [file for file in files if file != "__init__.py"]

        init_content = "\n".join([f"from .{file.replace('.py', '')} import *" for file in files])

        """ replace __init__.py and __init__.pyi """
        os.remove(f"{output_path}/__init__.py")
        os.remove(f"{output_path}/__init__.pyi")
        with open(f"{output_path}/__init__.py", "w+") as f:
            f.write(init_content)
            f.close()

        with open(f"{output_path}/__init__.pyi", "w+") as f:
            f.write(init_content)
            f.close()

    def find_py_dir(file_name: str):
        for item in api_definitions:
            output = f"{output_dir}/{item}"
            output_files = [
                file.replace(".py", "").replace(".pyi", "")
                for file in os.listdir(output)
                if file.endswith(".py") or file.endswith(".pyi")
            ]
            for file in output_files:
                if file == file_name:
                    """return dirname"""
                    return item
        return None

    """ fix all import in python files """
    for api_item in api_definitions:
        output_path = f"{output_dir}/{api_item}"
        files = [file for file in os.listdir(output_path) if file.endswith(".py") or file.endswith(".pyi")]
        for file in files:
            full_path = f"{output_path}/{file}"

            with open(full_path, "r") as f:
                lines = f.readlines()

            with open(full_path, "w") as f:
                for index, line in enumerate(lines):
                    import_name_regex = r"^import (.*) as (.*)$"
                    results = re.findall(import_name_regex, line)
                    if results:
                        import_name = results[0][0]
                        import_as_name = results[0][1]
                        py_dir = find_py_dir(import_name)
                        if py_dir:
                            line = f"from ..{py_dir} import {import_name} as {import_as_name}\n"
                            lines[index] = line
            with open(full_path, "w") as f:
                f.writelines(lines)
                f.close()


if __name__ == "__main__":
    run()
