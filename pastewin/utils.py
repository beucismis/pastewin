UNITS_MAPPING = [
    (1 << 50, " PB"),
    (1 << 40, " TB"),
    (1 << 30, " GB"),
    (1 << 20, " MB"),
    (1 << 10, " KB"),
    (1, (" Byte", " Bytes")),
]


def pretty_size(bytes, units=UNITS_MAPPING):
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
