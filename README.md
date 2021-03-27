# problems_ads

Algorithms and Data Structures problems and solutions from my personal study.

## Setup

```
pip install poetry
poetry install
```

## Running problems

```
pytest
```

## Adding problems and test scenarios

Adding a new problem is as simple as adding a new folder inside the `problems` folder with at least a python script for the solution, and a test scenario in the pattern `<scenario_name>.in` for input and `<scenario_name>.out` to the expected output.

As in this example:

```
problems
├── codeforces_101879_tea
│   ├── case_2_to_6.in
│   ├── case_2_to_6.out
│   ├── case_impossible.in
│   ├── case_impossible.out
│   ├── case_small1.in
│   ├── case_small1.out
│   ├── codeforces_101879_tea.py
│   └── problem.md
└── uri_2448_postman
    ├── case_large1.in
    ├── case_large1.out
    ├── case_large2.in
    ├── case_large2.out
    ├── case_small.in
    ├── case_small.out
    ├── case_small2.in
    ├── case_small2.out
    └── uri_2448_postman.py
```

Note: As I'm running the solution program using subprocess, It may support implementing solutions using other languages with changes in the collection method at `conftest.py`. Contributions are welcome.

All problems and test scenarios will be collected automatically when you run pytest using file pattern matching:

```
❯ pytest -v
======== test session starts ======== 
linux -- Python 3.8.1, pytest-6.2.2, py-1.10.0, pluggy-0.13.1 -- 
...
collected 7 items

test_contests.py::test_contests[problems/codeforces_101879_tea/codeforces_101879_tea.py-case_2_to_6] PASSED
tests.py::test_contests[problems/codeforces_101879_tea/codeforces_101879_tea.py-case_impossible] PASSED
test_contests.py::test_contests[problems/codeforces_101879_tea/codeforces_101879_tea.py-case_2_to_6] PASSED
tests.py::test_contests[problems/codeforces_101879_tea/codeforces_101879_tea.py-case_impossible] PASSED
tests.py::test_contests[problems/codeforces_101879_tea/codeforces_101879_tea.py-case_small1] PASSED
tests.py::test_contests[problems/uri_2448_postman/uri_2448_postman.py-case_large1] PASSED
tests.py::test_contests[problems/uri_2448_postman/uri_2448_postman.py-case_large2] PASSED
tests.py::test_contests[problems/uri_2448_postman/uri_2448_postman.py-case_small] PASSED
tests.py::test_contests[problems/uri_2448_postman/uri_2448_postman.py-case_small2] PASSED
```

You can also run benchmarks when running with:

``` 
 pytest --benchmark-enable
```

