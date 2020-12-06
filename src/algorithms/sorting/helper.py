def is_sorted(collection):
    return all(collection[i] <= collection[i + 1]
               for i in range(len(collection) - 1))
