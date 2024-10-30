import os
import shutil

import pytest

TEST_FILES_DIR = "test_files"


@pytest.fixture(scope="function")
def mock_test_file_folder():
    os.mkdir(TEST_FILES_DIR)
    yield
    shutil.rmtree(TEST_FILES_DIR)
