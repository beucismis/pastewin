import urllib3
from flask import abort


UNITS_MAPPING = [
    (1 << 50, " PB"),
    (1 << 40, " TB"),
    (1 << 30, " GB"),
    (1 << 20, " MB"),
    (1 << 10, " KB"),
    (1, (" Byte", " Bytes")),
]
http = urllib3.PoolManager()


def get_paste(id: str):
    r = http.request("GET", f"https://pastebin.com/raw/{id}")

    if r.status != 200:
        abort(404)

    return r


def pretty_size(bytes: int, units=UNITS_MAPPING):
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
