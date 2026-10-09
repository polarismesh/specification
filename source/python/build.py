"""Regenerate Python protobuf and gRPC stubs.

Requires grpcio-tools>=1.84.0 (protobuf>=7.35.1).
"""

import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
API_ROOT = REPO_ROOT / "api" / "v1"
OUTPUT_ROOT = REPO_ROOT / "source" / "python" / "src" / "polarismesh_specification" / "api" / "v1"

# proto directory under api/v1, extra include dirs under api/v1, output directory under OUTPUT_ROOT
API_DEFINITIONS = [
    ("model", []),
    ("fault_tolerance", ["model"]),
    ("traffic_manage", ["model"]),
    ("config_manage", ["model"]),
    ("security", ["model"]),
    (
        "service_manage",
        ["model", "traffic_manage", "fault_tolerance", "config_manage", "security"],
    ),
    ("traffic_manage/ratelimiter", []),
    ("skill_manage", []),
]


def grpc_well_known_proto_path() -> str:
    import grpc_tools

    return str(Path(grpc_tools.__file__).resolve().parent / "_proto")


def run_protoc(output_dir: Path, proto_paths: list[str], proto_files: list[str]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable,
        "-m",
        "grpc_tools.protoc",
        f"--python_out={output_dir}",
        f"--grpc_python_out={output_dir}",
        f"--pyi_out={output_dir}",
    ]
    for proto_path in proto_paths:
        command.append(f"--proto_path={proto_path}")
    command.extend(proto_files)
    subprocess.check_call(command)


def clean_generated(output_dir: Path) -> None:
    if not output_dir.exists():
        return
    for path in output_dir.iterdir():
        if not path.is_file():
            continue
        if path.name in {"__init__.py", "__init__.pyi"} or path.name.endswith(
            ("_pb2.py", "_pb2.pyi", "_pb2_grpc.py")
        ):
            path.unlink()


def write_init_files(output_dir: Path) -> None:
    modules = sorted(
        path.stem
        for path in output_dir.iterdir()
        if path.is_file() and path.suffix == ".py" and path.name != "__init__.py"
    )
    content = "".join(f"from .{module} import *\n" for module in modules)
    (output_dir / "__init__.py").write_text(content)
    (output_dir / "__init__.pyi").write_text(content)


def module_index(output_root: Path) -> dict[str, str]:
    """Map a generated module name to its package path relative to api/v1."""
    index: dict[str, str] = {}
    for path in output_root.rglob("*_pb2.py"):
        relative_dir = path.parent.relative_to(output_root).as_posix()
        index[path.stem] = "" if relative_dir == "." else relative_dir
    return index


def fix_imports(output_root: Path) -> None:
    index = module_index(output_root)
    import_pattern = re.compile(r"^import (\w+) as (\w+)$")

    for path in output_root.rglob("*"):
        if path.suffix not in {".py", ".pyi"} or not path.is_file():
            continue
        relative_dir = path.parent.relative_to(output_root).as_posix()
        depth = 1 if relative_dir == "." else len(Path(relative_dir).parts)
        dots = "." * (depth + 1)
        changed = False
        lines = path.read_text().splitlines(keepends=True)
        for index_no, line in enumerate(lines):
            matched = import_pattern.match(line.rstrip("\n"))
            if not matched:
                continue
            module_name, alias = matched.group(1), matched.group(2)
            package = index.get(module_name)
            if package is None:
                continue
            package_import = package.replace("/", ".")
            lines[index_no] = f"from {dots}{package_import} import {module_name} as {alias}\n"
            changed = True
        if changed:
            path.write_text("".join(lines))


def run() -> None:
    well_known = grpc_well_known_proto_path()
    for api_dir, relations in API_DEFINITIONS:
        proto_dir = API_ROOT / api_dir
        proto_files = sorted(path.name for path in proto_dir.glob("*.proto"))
        if not proto_files:
            raise FileNotFoundError(f"no proto files in {proto_dir}")

        output_dir = OUTPUT_ROOT / api_dir
        clean_generated(output_dir)
        proto_paths = [well_known, str(proto_dir)]
        proto_paths.extend(str(API_ROOT / relation) for relation in relations)
        run_protoc(output_dir, proto_paths, proto_files)
        write_init_files(output_dir)

    fix_imports(OUTPUT_ROOT)


if __name__ == "__main__":
    os.chdir(REPO_ROOT)
    run()
