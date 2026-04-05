def remove_duplicates(seq: list) -> list:
    removed = []
    for item in seq:
        if item not in removed:
            removed.append(item)
    return removed

def list_counts(seq: list) -> dict:
    count = {}
    for item in seq:
        if item in count:
            count[item] += 1  
        else:
            count[item] = 1  
    return count

def reverse_dict(d: dict) -> dict:
    reversed = {}
    for key, value in d.items():
        reversed[value] = key
    return reversed
