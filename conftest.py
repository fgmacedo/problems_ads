import shutil
import subprocess
from os import access, X_OK
from pathlib import Path

import pytest


SLICE_REMOVE_INPUT_EXTENSION = slice(0, -3)  # removes '.in'
SUPPORTED_EXTENSIONS = ["py", "cpp"]


def _is_executable(path):
    return access(path, X_OK)


def _compile_cpp(path):
    gpp = shutil.which("g++")

    output_file = path.with_suffix(".o")
    args = [gpp, "-std=c++11", "-O2", "-Wall", f"{path}", "-o", f"{output_file}"]
    res = subprocess.run(
        args,
        capture_output=True,
    )
    assert res.stderr == b"", ' '.join(args)
    assert res.returncode == 0
    return output_file


@pytest.fixture
def compiled_program(solution_path):
    if solution_path.suffix == ".py" and not _is_executable(solution_path):
        raise pytest.xfail(f"{solution_path} is not executable.")

    if solution_path.suffix == ".cpp":
        solution_path = _compile_cpp(solution_path)

    return solution_path


@pytest.fixture
def contest(benchmark, compiled_program):
    def run(input_path):
        comlist = [f"./{compiled_program}"]

        @benchmark
        def run_bench():
            with input_path.open("r") as input_file:
                res = subprocess.run(
                    comlist,
                    stdin=input_file,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )

            assert res.stderr == b""
            assert res.returncode == 0
            return res.stdout.decode("utf-8")

        return run_bench

    return run


def pytest_generate_tests(metafunc):
    if "contest" not in metafunc.fixturenames:
        return

    metafunc.parametrize(
        "solution_path, input_file, output_file",
        [
            pytest.param(
                solution_path,
                case,
                case.with_suffix(".out"),
                id=f"{solution_path}-{case.name[SLICE_REMOVE_INPUT_EXTENSION]}",
            )
            for extension in SUPPORTED_EXTENSIONS
            for solution_path in Path("problems").glob(f"**/*.{extension}")
            for case in solution_path.parent.glob("**/*.in")
        ],
    )
