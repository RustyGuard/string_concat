import subprocess

from app.bcolors import bcolors
from tests.fixtures import TEST_FILES_DIR, mock_test_file_folder


def test_minimal():
    result = subprocess.run(["python", "app/main.py", "a", "b"], capture_output=True)
    assert result.stdout == b"ab\n"


def test_write_to_file(mock_test_file_folder):
    data = b"ab"
    file_name = f"{TEST_FILES_DIR}/a.txt"
    subprocess.run(["python", "app/main.py", "a", "b", "--output", file_name])
    with open(file_name, mode="rb") as file:
        assert file.read() == data


def test_write_to_unknown_file(mock_test_file_folder):
    file_name = f"unknown/a.txt"
    result = subprocess.run(["python", "app/main.py", "a", "b", "--output", file_name], capture_output=True)
    assert result.stdout.decode("utf8") == f"{bcolors.FAIL}Несуществующий путь: unknown/a.txt{bcolors.ENDC}\n"
