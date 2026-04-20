from collections import defaultdict


def analyze_data(data):
    result = defaultdict(list)
    for item in data:
        result[item].append(item)
    return result
