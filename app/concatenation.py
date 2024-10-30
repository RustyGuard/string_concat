import sys


class NoStringsException(Exception):
    pass


def concat(*strings: str, separator: str = "", encoding: str = "utf8"):
    if not strings:
        raise NoStringsException
    result = separator.join(strings)
    result = result.encode(encoding)
    return result


def write_to_user(data: str | bytes, output: str | None):
    if output is None:
        sys.stdout.buffer.write(data)
        print()
        return

    with open(output, mode="wb") as file_to_write:
        file_to_write.write(data)
