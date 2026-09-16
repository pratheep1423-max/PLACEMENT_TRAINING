import subprocess
import sys
from pathlib import Path

root = Path(r"D:\placement-training")
question_files = sorted(root.glob("problem-*.py"))

sample_inputs = {
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

print("Select a question number to run (1-40), or type 'q' to quit.")
for i, path in enumerate(question_files, start=1):
    print(f"{i}. {path.name}")

while True:
    choice = input("\nEnter question number: ").strip().lower()
    if choice in ("q", "quit", "exit"):
        print("Exiting question runner.")
        break

    try:
        num = int(choice)
    except ValueError:
        print("Invalid input. Please enter a number from 1 to 40, or q.")
        continue

    if not (1 <= num <= len(question_files)):
        print("Number out of range. Please choose between 1 and 40.")
        continue

    target = question_files[num - 1]
    values = sample_inputs.get(target.name, ["0"])
    data = "\n".join(values) + "\n"
    print(f"\n=== Running {target.name} ===")
    result = subprocess.run([sys.executable, str(target)], input=data, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        print(f"Process exited with code {result.returncode}")
