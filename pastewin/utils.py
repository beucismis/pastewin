from os import environ
from flask import abort
from urllib3 import PoolManager


PORT = int(environ.get("PORT", 5000))
UNITS_MAPPING = [
    (1 << 50, " PB"),
    (1 << 40, " TB"),
    (1 << 30, " GB"),
    (1 << 20, " MB"),
    (1 << 10, " KB"),
    (1, (" Byte", " Bytes")),
]
ENDPOINT = "https://pastebin.com/raw/{}"

http = PoolManager()


def paste_content(id: str) -> str:
    response = http.request("GET", ENDPOINT.format(id))

    if response.status != 200:
        abort(404)

    return response.data


def pretty_size(bytes: int, units: list = UNITS_MAPPING) -> str:
    # Source: https://stackoverflow.com/a/12912296

    bytes = len(bytes.encode("utf-8"))

    for factor, suffix in units:
        if bytes >= factor:
            break

    amount = int(bytes / factor)

    if isinstance(suffix, tuple):
        singular, multiple = suffix

        if amount == 1:
            suffix = singular
        else:
            suffix = multiple

    return str(amount) + suffix
