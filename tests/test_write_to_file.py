from app import concatenation
from tests.fixtures import TEST_FILES_DIR, mock_test_file_folder


def test_print(capsys):
    concatenation.write_to_user(b"abc", output=None)
    assert capsys.readouterr().out == "abc\n"


def test_write_file(mock_test_file_folder):
    file_name = f"{TEST_FILES_DIR}/a.txt"
    data = b"abc"
    concatenation.write_to_user(data, output=file_name)
    with open(file_name, mode="rb") as file:
        assert file.read() == data
