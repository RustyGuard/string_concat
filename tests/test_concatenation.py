import pytest

from app import concatenation
from app.concatenation import NoStringsException


def test_without_strings():
    """Ввод нуля строк недопустим"""
    with pytest.raises(NoStringsException):
        concatenation.concat(separator="\n")


def test_basic_concat():
    assert concatenation.concat("a", "b") == b"ab"


def test_with_separator():
    assert concatenation.concat("a", "b", separator="\n") == b"a\nb"


@pytest.mark.parametrize("strings,separator,expected_result", (
        (["a"], "\n", b"a"),
        (["a", "b"], " ", b"a b"),
        (["a", "b"], "\n", b"a\nb"),
        (["a", "b", "c"], "", b"abc"),
))
def test_parametrized(strings: list[str], separator: str, expected_result: str):
    assert concatenation.concat(*strings, separator=separator) == expected_result


def test_with_ascii():
    assert concatenation.concat("a", "b", encoding="ascii") == b"ab"
    with pytest.raises(UnicodeEncodeError):
        concatenation.concat("а", "я", encoding="ascii")


def test_with_cp1251():
    assert concatenation.concat("a", "b", encoding="cp1251") == b"ab"
    assert concatenation.concat("а", "я", encoding="cp1251") == b"\xe0\xff"


def test_with_iso8859_1():
    assert concatenation.concat("a", "b", encoding="iso8859_1") == b"ab"
    with pytest.raises(UnicodeEncodeError):
        concatenation.concat("а", "я", encoding="iso8859_1")


def test_with_unknown_encoding():
    with pytest.raises(LookupError):
        concatenation.concat("а", "я", encoding="hehehe")
