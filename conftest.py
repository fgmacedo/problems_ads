import pytest
import subprocess
from pathlib import Path


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

    metafunc.parametrize("program", ["uri_2448_postman/uri_2448_postman.py"])

    metafunc.parametrize("input_file, output_file", [
        pytest.param(
            Path(f"uri_2448_postman/case_{item}_input.txt"),
            Path(f"uri_2448_postman/case_{item}_output.txt"),
            id=f"{item}",
        )
        for item in ["small", "small2", "large1", "large2", ]
    ])
