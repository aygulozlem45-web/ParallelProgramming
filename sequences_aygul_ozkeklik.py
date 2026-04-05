def remove_duplicates(seq: list) -> list:
    return list(dict.fromkeys(seq))

def list_counts(seq: list) -> dict:
    return {x: seq.count(x) for x in set(seq)}

def reverse_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}
