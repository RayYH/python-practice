def linear_search(collection, target):
    for i in range(0, len(collection)):
        if collection[i] == target:
            return i
    return None
