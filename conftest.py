import pytest
import subprocess
from pathlib import Path


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

    programs = Path("problems").glob("**/*.py")

    for program in programs:
        metafunc.parametrize("program", [
            pytest.param(program, id=f"{program}"),
        ])

        cases = program.parent.glob("**/*.in")

        metafunc.parametrize("input_file, output_file", [
            pytest.param(
                item,
                item.with_suffix(".out"),
                id=f"{item.name[SLICE_REMOVE_INPUT_PREFIX_AND_SUFFIX]}",
            )
            for item in cases
        ])
