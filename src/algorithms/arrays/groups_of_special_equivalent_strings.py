from typing import List


def num_of_special_equivalent_strings(collection: List[str]) -> int:
    """
    https://leetcode.com/problems/groups-of-special-equivalent-strings/
    """
    def count(word):
        ans = [0] * 52
        for j, letter in enumerate(word):
            ans[ord(letter) - ord('a') + 26 * (j % 2)] += 1
        return tuple(ans)

    return len({count(word) for word in collection})
