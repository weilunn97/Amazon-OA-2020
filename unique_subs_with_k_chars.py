from typing import List


def unique_subs_with_k_chars(s: str, k: int) -> List[str]:
    """
    Time  : O(N)
    Space : O(1), where N = len(s)
    """
    res = []
    res_set = set()
    # TRY EACH POSSIBLE SUBSTRING
    for i in range(len(s) - k + 1):
        substring = s[i: i + k]
        if len(set(substring)) == k:
            if substring not in res_set:
                res.append(substring)
                res_set.add(substring)
    return res


if __name__ == "__main__":
    print(unique_subs_with_k_chars("abcabc", 3) == ["abc", "bca", "cab"])
    print(unique_subs_with_k_chars("abacab", 3) == ["bac", "cab"])
    print(
        unique_subs_with_k_chars("awaglknagawunagwkwagl", 4) == ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun",
                                                                 "wuna", "unag", "nagw", "agwk", "kwag"])
