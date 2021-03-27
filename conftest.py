import subprocess
from pathlib import Path

import pytest


SLICE_REMOVE_INPUT_PREFIX_AND_SUFFIX = slice(0, -3)


@pytest.fixture
def contest(benchmark):

    def run(contest, input_path):
        comlist = [f"./{contest}"]

        @benchmark
        def run_bench():
            with input_path.open('r') as input_file:
                res = subprocess.run(comlist, stdin=input_file,
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert res.stderr == b''
            assert res.returncode == 0
            return res.stdout.decode("utf-8")

        return run_bench

    return run


def pytest_generate_tests(metafunc):
    if "program" not in metafunc.fixturenames:
        return

    metafunc.parametrize("program, input_file, output_file", [
        pytest.param(
            program,
            case,
            case.with_suffix(".out"),
            id=f"{program}-{case.name[SLICE_REMOVE_INPUT_PREFIX_AND_SUFFIX]}",
        )
        for program in Path("problems").glob("**/*.py")
        for case in program.parent.glob("**/*.in")
    ])
