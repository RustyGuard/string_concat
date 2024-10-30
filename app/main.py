import typer

import concatenation
from bcolors import bcolors

app = typer.Typer()


@app.command()
def main(strings: list[str], output: str | None = None, encoding: str = "utf8", sep: str = ""):
    if output is None and encoding != "utf8":
        print(f"{bcolors.FAIL}Невозможно указать кодировку без указания выходного файла{bcolors.ENDC}")
        return
    try:
        result_string = concatenation.concat(*strings, encoding=encoding, separator=sep)
    except UnicodeEncodeError:
        print(f"{bcolors.FAIL}Невозможно привести строку к формату: {encoding}{bcolors.ENDC}")
        return
    except LookupError:
        print(f"{bcolors.FAIL}Неизвестный формат: {encoding}{bcolors.ENDC}")
        return
    try:
        concatenation.write_to_user(result_string, output)
    except PermissionError:
        print(f"{bcolors.FAIL}Файл недоступен для записи: {output}{bcolors.ENDC}")
        return
    except FileNotFoundError:
        print(f"{bcolors.FAIL}Несуществующий путь: {output}{bcolors.ENDC}")
        return


if __name__ == "__main__":
    app()
