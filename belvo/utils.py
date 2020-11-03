import pathlib
from base64 import b64encode


def read_file_to_b64(path: str):
    file = pathlib.Path(path)
    if file.exists() and file.is_file():
        with open(path, "rb") as fr:
            return b64encode(fr.read())
    else:
        raise ValueError("Invalid file path")


def clean_none_values(data):
    return {key: value for key, value in data.items() if value is not None}
