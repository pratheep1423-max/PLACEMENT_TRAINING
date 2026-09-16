import builtins
import importlib.util
import io
from contextlib import redirect_stdout, redirect_stderr
from pathlib import Path

root = Path(r"D:\placement-training")

cases = {
    "problem-01.py": ["12"],
    "problem-02.py": ["-7"],
    "problem-03.py": ["15", "25"],
    "problem-04.py": ["10", "20", "30"],
    "problem-05.py": ["9", "12", "18"],
    "problem-06.py": ["25"],
    "problem-07.py": ["55"],
    "problem-08.py": ["2024"],
    "problem-09.py": ["13"],
    "problem-10.py": ["28"],
    "problem-11.py": ["153"],
    "problem-12.py": ["121"],
    "problem-13.py": ["145"],
    "problem-14.py": ["5"],
    "problem-15.py": ["9"],
    "problem-16.py": ["456"],
    "problem-17.py": ["456"],
    "problem-18.py": ["4567"],
    "problem-19.py": ["456"],
    "problem-20.py": ["456"],
    "problem-21.py": ["456"],
    "problem-22.py": ["1234"],
    "problem-23.py": ["1234"],
    "problem-24.py": ["2468"],
    "problem-25.py": ["1357"],
    "problem-26.py": ["327"],
    "problem-27.py": ["327"],
    "problem-28.py": ["1223", "2"],
    "problem-29.py": ["1205"],
    "problem-30.py": ["12345"],
    "problem-31.py": ["10"],
    "problem-32.py": ["10"],
    "problem-33.py": ["10"],
    "problem-34.py": ["10"],
    "problem-35.py": ["10"],
    "problem-36.py": ["10"],
    "problem-37.py": ["10"],
    "problem-38.py": ["5"],
    "problem-39.py": ["7"],
    "problem-40.py": ["20"],
}

for file_path in sorted(root.glob("problem-*.py")):
    name = file_path.name
    values = cases.get(name, ["0"])
    iterator = iter(values)

    def fake_input(prompt=""):
        try:
            return next(iterator)
        except StopIteration:
            return "0"

    original_input = builtins.input
    builtins.input = fake_input
    try:
        spec = importlib.util.spec_from_file_location(name[:-3], file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        stdout = io.StringIO()
        stderr = io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            module.main()

        print(f"\n=== {name} ===")
        printed = stdout.getvalue().strip()
        if printed:
            print(printed)
        else:
            print("(no output)")
    finally:
        builtins.input = original_input
