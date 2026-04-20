import os
import sys  
from collections import defaultdict

unused_var = 42

def analyze_data(data):
    result = defaultdict(list)
    for item in data:
        result[item].append(item)
    return result
